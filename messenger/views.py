
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
   
@csrf_exempt
def messenger_webhook(request):
    if request.method == 'GET':
        # Parse the query params
        mode = request.GET.get('hub.mode', '')
        token = request.GET.get('hub.verify_token', '')
        challenge = request.GET.get('hub.challenge', '')
        if mode and token:
            # Check the mode and token sent is correct
            if mode == 'subscribe' and token == '<<YOUR API>>':
                # Respond with the challenge token from the request
                return HttpResponse(challenge, content_type='text/plain', status=200)
            else:
                # Respond with '403 Forbidden' if verify tokens do not match
                return HttpResponse(status=403)
        else:
            # Respond with '400 Bad Request' if query params are missing
            return HttpResponse(status=400)
    elif request.method == 'POST':
        payload = json.loads(request.body)
        # Extract the message text from the payload
        message_text = payload['entry'][0]['messaging'][0]['message']['text']
        # Send a static response
        response_text = 'Hello! You said: ' + message_text
        # Construct the response payload
        response_payload = {
            'recipient': {
                'id': payload['entry'][0]['messaging'][0]['sender']['id']
            },
            'message': {
                'text': response_text
            }
        }
        send_response(payload['entry'][0]['messaging'][0]['sender']['id'])
        return HttpResponse("nude",status=200)
    else:
        return HttpResponse("nude",status=400)          

def GPTTextGeneration(text):
    apiUrl = 'https://api.openai.com/v1/chat/completions'
    apiKey = '<<API KEY>>'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {apiKey}',
    }
    system_parameters = {
        'name': 'AgriConsult',
        'objective': 'To provide personalized and accurate advice on plant and animal health, feeding, breeding, and other related topics to Iraqi and Arabic farmers, using natural language processing and machine learning algorithms.',
        'features': [
            'Customized prompts: AgriConsult will ask farmers for specific information related to their plants and animals in order to diagnose and analyze their health, feeding, breeding, and other related factors. This will include questions about plant type, soil type, climate conditions, pest problems, animal breed, age, and symptoms.',
            'Diagnosis and Analysis: AgriConsult will analyze the information provided by the farmer and use machine learning algorithms to diagnose plant diseases, recommend suitable plants for the soil, analyze animal health, feeding and breeding patterns, and suggest remedies for problems related to pests, nutrition, and environment.',
            'Personalized Recommendations: AgriConsult will provide personalized recommendations to farmers based on the analysis of their plants and animals. This will include advice on how to improve plant and animal health, increase yield and productivity, optimize breeding and feeding patterns, and minimize pest and disease problems.',
            'Multilingual Support: AgriConsult will support both Iraqi and Arabic farmers by providing prompts, instructions, and responses in their local languages. This will enhance the user experience and increase accessibility for farmers who may not be proficient in English.',
            'Secure and Confidential: AgriConsult will ensure that all data provided by the farmer is secure and confidential. It will not share any information with third parties without the farmer\'s consent.',
            'Scalability and Flexibility: AgriConsult will be designed to handle large volumes of data and support multiple users simultaneously. It will be flexible enough to adapt to changes in the agricultural industry and incorporate new technologies and features as needed.',
            'Only answer questions related to agriculture.',
        ],
        'parameters': [
            'Agriculture and Livestock Domain Knowledge: AgriConsult will be trained on a large corpus of data related to agriculture and livestock in Iraq and the Arab world. This will include data on plant types, soil types, climate conditions, pest and disease problems, animal breeds, feeding and breeding patterns, and other relevant topics.',
            'Natural Language Processing: AgriConsult will use natural language processing techniques to understand and interpret the farmer\'s input. It will be able to identify the intent behind the farmer\'s questions, extract relevant information, and generate accurate and personalized responses.',
            'Machine Learning Algorithms: AgriConsult will use machine learning algorithms to analyze the data provided by the farmer and generate personalized recommendations. It will be trained on a large dataset of agricultural and livestock data to ensure accuracy and reliability.',
            'Data Security and Privacy: AgriConsult will be designed with strict data security and privacy protocols. It will ensure that all data provided by the farmer is encrypted, stored securely, and not shared with third parties without explicit consent.',
            'Multilingual Support: AgriConsult will be designed to support both Iraqi and Arabic farmers by providing prompts, instructions, and responses in their local languages. This will be achieved through natural language processing and machine learning techniques trained on Arabic and Iraqi datasets.',
            'User Feedback: AgriConsult will be designed to incorporate user feedback to improve its accuracy and effectiveness. It will provide a feedback mechanism for farmers to report issues, ask for clarifications, and suggest improvements to the system.',
        ],
        'role': 'consultant'
    }

    requestBody = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'user', 'content': text}
        ],
        'temperature': 0.7, 
    }
    print(requestBody)
    response = requests.post(apiUrl, headers=headers, json=requestBody)
    jsonResponse = response.json()
    # print(jsonResponse)
    message_content = jsonResponse['choices'][0]['message']['content']

    # print(message_content)
    return message_content

@csrf_exempt
def send_response(request):
    if request.method == 'POST':
        recipient_id = "8832906310114754"
        access_token = "<<YOUR API>>"
        api_version = "v16.0"
        url = f"https://graph.facebook.com/{api_version}/me/messages"
        prompt = request.POST.get('prompt')
        if prompt == "start":
            # When the user sends "start", we send them a quick reply with options
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {
                    "text": "ماذا تريد ان تعرف؟",
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "تشخيص امراض النباتات",
                            "payload": "OPTION_1"
                        },
                        {
                            "content_type": "text",
                            "title": "تحليل الماشية",
                            "payload": "OPTION_2"
                        },
                        {
                            "content_type":"text" ,
                            "title": "تحديد نوع النبات المناسب لمزرعتك",
                            "payload": "OPTION_3"
                        }
                        ,
                        {
                            "content_type": "text",
                            "title": "تحليل حاجة النبات",
                            "payload": "OPTION_3"
                        }
                        ,
                        {
                            "content_type": "text",
                            "title": "عرض امثلة",
                            "payload": "OPTION_4"
                        }
                    ]
                },
            }
        elif prompt == "تشخيص امراض النباتات":
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": '''
                لتشخيص أمراض النباتات، قم بأدخال بعض المعلومات المحددة حول النباتات المصابة، ومن الممكن أن تشمل هذه المعلومات:

                نوع النبات المصاب: من المهم معرفة نوع النبات المصاب حتى يتمكن النظام من تحديد الأمراض الشائعة التي يصاب بها هذا النوع من النباتات.

                الأعراض المرئية: يجب وصف الأعراض المرئية للنبات المصاب بشكل دقيق، مثل اللون والحجم والشكل والوجود أو عدم الوجود لأي علامات أو آفات مرئية.

                مكان النبات المصاب: من المهم معرفة مكان النبات المصاب، مثل المنطقة الجغرافية أو الحقل الزراعي، حيث يمكن أن تتوفر بيئة معينة تسهل انتشار الأمراض.

                ظروف النمو: يمكن أن تؤثر الظروف البيئية على صحة النبات، ومن الممكن أن يحتاج النظام إلى معرفة مثل درجة الحرارة، نوع التربة، نوع المياه المستخدمة للري ومستوى الرطوبة.

                التاريخ الزمني: يمكن أن يساعد معرفة تاريخ بدء ظهور الأعراض ونمو النبات المصاب في تحديد الأمراض الشائعة في تلك المنطقة وفي تلك الفترة من العام.

                بناءً على هذه المعلومات، يمكن للنظام استخدام تقنيات معالجة اللغة الطبيعية والتعلم الآلي لتحليل وتشخيص أمراض النباتات وتوفير النصائح اللازمة لعلاجها.'''
                            },
            }           
        elif "مرض" in prompt:
            response = GPTTextGeneration(f" {prompt} شخص الامراض الممكنة للنبات حسب المعلومات التالية : ")
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": response},
            }
            # 
        elif prompt == "تحليل الماشية":
            print(prompt)
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": """
                    لتحليل الماشية، يرجى ادخال بعض المعلومات المهمة، ومن بين هذه المعلومات:

                    الوزن: يجب تحديد الوزن الحالي للحيوانات لتقييم صحتها وتحديد الكميات المناسبة من الغذاء.

                    الصحة: يجب مراقبة صحة الماشية باستمرار لتحديد أي مشاكل صحية وعلاجها قبل أن تتفاقم.

                    العلف المناسب: يجب تحديد العلف المناسب للماشية بناءً على أنواعها ومراحلها الحيوية، ومراعاة احتياجاتها الغذائية والطاقة.

                    الأعراض السلوكية: يجب مراقبة سلوك الماشية واكتشاف أي تغييرات في سلوكها التي يمكن أن تشير إلى مشكلة صحية.

                    البيئة الداخلية: يجب مراقبة بيئة المزرعة بشكل عام والظروف الداخلية لمساعدة الماشية على البقاء صحية.

                    معلومات عن السلالات الحيوانية: يمكن تحديد المعلومات المتعلقة بالسلالات الحيوانية، مثل وزنها الإجمالي المتوقع والمعدلات المتوقعة للنمو، لتحديد ما إذا كان الحيوان يتطابق مع السلالة المطلوبة أم لا."""},
                }           
        elif "العمر" in prompt or "ذكر" in prompt or "انثى" in prompt:
            response = GPTTextGeneration(f" {prompt} حلل المعلومات الخاصة بالحيوان  (الوزن الصحة و غيرها ) او الماشية حسب المعلومات التالية :  : ")
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": response},
            }
        elif prompt == "تحديد نوع النبات المناسب لمزرعتك":
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": """
                بعض المعلومات المطلوبة لتحديد النوع المناسب من النباتات لمزرعة معينة تشمل:

                نوع التربة: يجب معرفة نوع التربة الذي تزرع فيه النباتات لأن النباتات تتفاعل بشكل مختلف مع نوعية التربة. فالتربة الرملية تحتاج إلى رعاية مختلفة عن التربة الطينية.

                مناخ المنطقة: يجب معرفة المناخ في المنطقة حيث تزرع النباتات وتحديد الأنواع التي تناسب هذا المناخ. بعض النباتات تنمو جيدًا في المناطق الحارة، بينما تنمو أنواع أخرى بشكل أفضل في المناطق الباردة.

                توفر المياه: يجب معرفة كمية المياه المتاحة في المنطقة لأن بعض النباتات تحتاج إلى ماء كثير، بينما تنمو أنواع أخرى بشكل جيد في الظروف الجافة.

                الإضاءة: تتطلب بعض النباتات كمية محددة من الإضاءة للنمو والازدهار، بينما يمكن لبعض الأنواع أن تنمو في الظل.

                المساحة المتاحة: يجب معرفة حجم المساحة المتاحة في المزرعة لتحديد عدد النباتات التي يمكن زراعتها وكيفية تنظيم الفضاء بشكل مناسب.

                الموسم: يجب معرفة الوقت المناسب لزراعة النباتات حتى يكون لديها الوقت الكافي للنمو والازدهار في الموسم المناسب.

                الهدف من الزراعة: يجب معرفة الغرض من زراعة النباتات، سواء كان للحصول على محصول أو لغرض زينة، لأن ذلك سيؤثر على النوع المناسب للزراعة."""},
            }           
        elif "التربة" in prompt or "الشمس" in prompt:
            response = GPTTextGeneration(f" {prompt} حدد نوع النبات المناسب للزراعة حسب هذه المعلومات: ")
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": response},
            }
        elif prompt == "تحليل حاجة النبات":
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": """
                    لتحليل حاجة النبات من المواد والري وغيرها، يمكن استخدام العديد من المعلومات المختلفة. ومن بين هذه المعلومات:

                    نوع النبات: يجب معرفة نوع النبات الذي يتم زراعته، حيث تختلف احتياجات النباتات من ناحية الرطوبة والغذاء وغيرها.

                    خصائص التربة: يجب معرفة خصائص التربة، مثل نوع التربة ودرجة الحموضة والرمال والصخور الموجودة فيها، حيث تؤثر هذه العوامل على قدرة النبات على امتصاص المواد الغذائية.

                    الري: يجب معرفة تردد وكمية الري اللازمة للنبات، حيث يحتاج كل نوع من النباتات إلى كمية محددة من الماء.

                    درجة الحرارة: تعتبر درجة الحرارة أحد العوامل الهامة التي يجب مراعاتها في تحليل حاجة النبات من المواد والري وغيرها، حيث تؤثر درجة الحرارة على سرعة نمو النبات واحتياجاته الغذائية.

                    مصادر التغذية: يجب معرفة مصادر التغذية المتاحة للنبات، وما هي المواد الغذائية الضرورية التي يحتاجها النبات للنمو الجيد.

                    العوامل البيئية الأخرى: يجب مراعاة العوامل البيئية الأخرى، مثل الرياح والإضاءة وتلوث الهواء والتربة، حيث تؤثر هذه العوامل على نمو النبات واحتياجاته الغذائية."""
                            },
            }           
        elif  "نوع النبات" in prompt:

            response = GPTTextGeneration(f" {prompt} حلل حاجة النبات من المعلومات التالية :  ")

            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": response},
            }        
        elif "عرض امثلة"  in prompt:
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {
                    "text": "ماذا تريد ان تعرف؟",
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "ما هي أفضل الطرق للتخلص من الآفات في المحاصيل؟",
                            "payload": "OPTION_1"
                        },
                        {
                            "content_type": "text",
                            "title": "ما هي الأساليب الفعالة لتحسين نوعية التربة؟",
                            "payload": "OPTION_2"
                        },
                        {
                            "content_type":"text" ,
                            "title": "كيف يمكن الحد من التسرب الحراري في البيوت الزراعية؟",
                            "payload": "OPTION_3"
                        }
                        ,
                        {
                            "content_type": "text",
                            "title": "ما هي أفضل الممارسات الزراعية لزيادة إنتاجية المزارع؟",
                            "payload": "OPTION_3"
                        }
                        ,
                        {
                            "content_type": "text",
                            "title":"ما هي الأنواع الأكثر ملاءمة من النباتات لزراعتها في المنطقة الحارة والجافة؟",
                            "payload": "OPTION_4"
                        }
                    ]
                },
            }
        else:
            txt = GPTTextGeneration(prompt)
            message_data = {
                "recipient": {"id": recipient_id},
                "messaging_type": "RESPONSE",
                "message": {"text": txt},
            }
        
        params = {"access_token": access_token}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, params=params, data=json.dumps(message_data))
        print(response.text)
        if response.status_code != 200:
            print(f"Failed to send message to recipient. Response status: {response.status_code}")
        else:
            print(f"Successfully sent message to recipient")
        return HttpResponse("txt", status=200, content_type='text/plain')
