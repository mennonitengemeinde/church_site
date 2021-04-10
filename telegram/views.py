# import json
# import logging
#
# from django.conf import settings
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
#
# import telebot
#
# BOT_TOKEN = '219325259:AAGBwcfqQCTvLkKwKkcJDRrse0z3o95OznQ'
#
# logger = telebot.logger
# telebot.logger.setLevel(logging.INFO)
# bot = telebot.TeleBot(settings.WOL_EVENTS_BOT_TOKEN)
#
#
# @csrf_exempt
# def webhook(request):
#     if request.method == 'POST':
#         if request.headers.get('content-type') == 'application/json':
#             json_data = request.body.decode('utf-8')
#             update = telebot.types.Update.de_json(json_data)
#             bot.process_new_updates([update])
#             return JsonResponse({})
#         else:
#             return JsonResponse({'message': 'content-type is not acceptable'}, status=403)
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, 'What is your preferred language?')
#
#
# # Handle all other messages
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def echo_message(message):
#     bot.send_message(message.chat.id, message.text)
#     # bot.reply_to(message, message.text)
