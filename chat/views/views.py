import os
import json
import openai
import datetime
import tiktoken
from chat.models import Conversation, Message, Setting, Prompt
from django.conf import settings
from django.http import StreamingHttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from chat.serializers import ConversationSerializer, MessageSerializer, PromptSerializer, SettingSerializer
from utils.search_prompt import compile_prompt
from utils.duckduckgo_search import web_search, SearchRequest


class SettingViewSet(viewsets.ModelViewSet):
    serializer_class = SettingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        available_names = [
            'open_registration',
            'open_web_search',
            'open_api_key_setting'
        ]
        return Setting.objects.filter(name__in=available_names)

    def http_method_not_allowed(self, request, *args, **kwargs):
        if request.method != 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().http_method_not_allowed(request, *args, **kwargs)


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user).order_by('-created_at')

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        queryset.delete()
        return Response(status=204)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        conversationId = self.request.query_params.get('conversationId')
        if conversationId:
            queryset = queryset.filter(conversation_id=conversationId).order_by('created_at')
        return queryset


class PromptViewSet(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prompt.objects.filter(user=self.request.user).order_by('-created_at')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['user'] = request.user

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        queryset.delete()
        return Response(status=204)




