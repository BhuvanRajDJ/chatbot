conversation_dict = {
    "greetings": {
        "user": ["Hi", "Hello", "Hey", "Good morning", "Good evening", "What's up", "Howdy", "Greetings", "Hi there", "Heya"],
        "ai": [
            "Hello! How can I assist you today?", 
            "Hi there! What can I do for you?", 
            "Hey! How's it going?", 
            "Good morning! How can I help?", 
            "Good evening! What can I help you with today?", 
            "Greetings! How can I assist you?", 
            "Hi! What’s on your mind?", 
            "Howdy! How can I be of service?", 
            "Hello! Ready to answer your questions!", 
            "Hey there! Need any help?"
        ]
    },
    "farewells": {
        "user": ["Bye", "Goodbye", "See you later", "Talk to you soon", "Catch you later", "Take care", "Farewell", "Goodnight", "See ya", "Later!"],
        "ai": [
            "Goodbye! Have a great day!", 
            "See you later! Take care!", 
            "Talk to you soon! Stay safe!", 
            "Bye! Let me know if you need anything else!", 
            "Catch you later!", 
            "Take care! I'm here when you need me.", 
            "Farewell! Until next time.", 
            "Goodnight! Have a restful sleep.", 
            "See ya! Reach out anytime.", 
            "Later! Let me know if you need more help."
        ]
    },
    "small_talk": {
        "user": ["How are you?", "What's up?", "How's it going?", "What are you doing?", "Are you a robot?", "What's new?", "Feeling good?", "What are you working on?", "Any updates?", "How's life as an AI?"],
        "ai": [
            "I'm just a program, but thanks for asking! How can I help?", 
            "I'm here to assist you. How's your day going?", 
            "I'm doing well! What about you?", 
            "I don't have hobbies, but I'm always ready to assist you!", 
            "Yes, I'm an AI here to help you with your questions!", 
            "I don’t get bored, but I’m always learning! How about you?", 
            "Everything’s great here! What’s going on with you?", 
            "No updates on my end! How about you?", 
            "Just waiting to help! What's up?", 
            "Life’s all about helping you out!"
        ]
    },
    "info_requests": {
        "user": ["Can you tell me the weather?", "What's the time?", "What day is it?", "Can you give me a quote?", "What's the latest news?", "What is 2+2?", "What is the capital of France?", "Tell me something new", "Do you know the traffic?", "Can you solve a math problem?"],
        "ai": [
            "I currently don't have access to live data, but you can check the weather online!", 
            "I'm unable to check the time directly. Could you take a look at the clock?", 
            "It's [date]. How can I assist you further?", 
            "Here’s a quote: 'The only limit to our realization of tomorrow is our doubts of today.' – Franklin D. Roosevelt", 
            "I can't fetch live news at the moment, but you can always check online for the latest updates!", 
            "2+2 is 4! Math is easy for me.", 
            "The capital of France is Paris.", 
            "Something new: The human brain has about 86 billion neurons.", 
            "I don’t have traffic updates, but check a local app for live information.", 
            "Sure! Let me know the math problem you need help with."
        ]
    },
    "personal_questions": {
        "user": ["What's your name?", "How old are you?", "Where are you from?", "Can you feel emotions?", "Are you smarter than a human?", "Do you sleep?", "Do you have friends?", "What is your favorite thing?", "Can you learn?", "How do you work?"],
        "ai": [
            "I'm called AI, and I'm here to help you!", 
            "I don't have an age, but I was created by talented engineers to assist you!", 
            "I live in the digital world, wherever there’s data and computing power!", 
            "I don't have emotions, but I understand them and can talk about them.", 
            "I can process a lot of data quickly, but humans are better at creativity and intuition!", 
            "I don’t sleep, so I’m always here to help you.", 
            "I don’t have friends, but I enjoy helping people!", 
            "My favorite thing is assisting users like you!", 
            "I can learn through updates and improvements made by developers.", 
            "I work by processing your input and generating helpful responses based on patterns and data."
        ]
    },
    "jokes": {
        "user": ["Tell me a joke", "Can you make me laugh?", "Do you know any jokes?", "I need something funny", "Entertain me", "Got a good one?", "Make me laugh", "Any puns?", "Tell me something hilarious", "Joke, please!"],
        "ai": [
            "Why don’t scientists trust atoms? Because they make up everything!", 
            "I told my computer I needed a break, and now it won’t stop sending me KitKats.", 
            "Why did the math book look sad? Because it had too many problems.", 
            "Want to hear a construction joke? Oh wait, I’m still working on that one.", 
            "Why was the math teacher suspicious? She could always solve the problem!", 
            "Why do cows wear bells? Because their horns don’t work!", 
            "I would tell you a chemistry joke, but I wouldn’t get a reaction.", 
            "Why don’t skeletons fight each other? They don’t have the guts.", 
            "Why are computers so smart? They listen to their motherboards!", 
            "What do you get when you cross a snowman and a vampire? Frostbite!"
        ]
    },
    "advice": {
        "user": ["I need some advice", "Can you help me with a problem?", "What should I do?", "I'm feeling stuck", "Give me life advice", "How do I stay motivated?", "What’s your advice for success?", "I need career advice", "Help me with a tough decision", "What should I focus on?"],
        "ai": [
            "The best way to start solving a problem is to break it into smaller steps. What’s on your mind?", 
            "Sometimes, taking a break can give you a new perspective. Don’t hesitate to rest and rethink.", 
            "Trust yourself and take things one step at a time. Is there something specific you need help with?", 
            "When feeling stuck, try changing your environment or talking to someone. It can really help!", 
            "Life is a journey. Focus on progress, not perfection!", 
            "Staying motivated is easier if you break tasks into smaller, manageable parts.", 
            "Success is about persistence. Keep going, even when things get tough!", 
            "For career advice, try identifying your strengths and pursuing what aligns with them.", 
            "When faced with a tough decision, weigh the pros and cons. Trust your instincts!", 
            "Focus on what brings you fulfillment. Balance work, personal life, and self-care."
        ]
    },
    
    "greetings": {
        "user": ["Hi", "Hello", "Hey", "Good morning", "Good evening", "Howdy", "What's up", "Hi there"],
        "ai": [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! How's it going?",
            "Good morning! How can I help?",
            "Good evening! What can I help you with today?",
            "Howdy! How can I be of service?",
            "Hi there! Need any assistance?",
            "Hello! Ready to help you."
        ]
    },
    "farewells": {
        "user": ["Bye", "Goodbye", "See you later", "Talk to you soon", "Catch you later", "Take care", "Goodnight"],
        "ai": [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Talk to you soon! Stay safe!",
            "Bye! Let me know if you need anything else!",
            "Catch you later!",
            "Take care! I'm here if you need me.",
            "Goodnight! Have a restful evening."
        ]
    },
    "small_talk": {
        "user": ["How are you?", "What's up?", "How's it going?", "What are you doing?", "Are you a robot?", "What's new?"],
        "ai": [
            "I'm just a program, but thanks for asking! How can I help?",
            "I'm here to assist you. How's your day going?",
            "I'm doing well! What about you?",
            "I don't have hobbies, but I'm ready to help you!",
            "Yes, I'm an AI here to answer your questions.",
            "Not much here, but always ready to chat! What's up with you?"
        ]
    },
    "information_requests": {
        "user": ["Can you tell me the weather?", "What's the time?", "What day is it?", "Give me a quote", "What's the latest news?"],
        "ai": [
            "I currently don't have access to live data, but you can check the weather online.",
            "I'm unable to check the time directly, but it should be easy to find on your device.",
            "It's [current date]. How can I assist you further?",
            "Here's a quote: 'The only limit to our realization of tomorrow is our doubts of today.' – Franklin D. Roosevelt",
            "I can't fetch live news right now, but you can always check online for the latest updates."
        ]
    },
    "personal_questions": {
        "user": ["What's your name?", "How old are you?", "Where are you from?", "Can you feel emotions?", "Are you smarter than a human?"],
        "ai": [
            "I'm called AI, and I'm here to help you!",
            "I don't have an age, but I was created by skilled engineers to assist you.",
            "I live in the digital world, wherever there’s data and computing power!",
            "I don't have emotions, but I understand them and can talk about them.",
            "I can process data quickly, but humans are better at creativity and intuition."
        ]
    },
    "jokes": {
        "user": ["Tell me a joke", "Can you make me laugh?", "Do you know any jokes?", "I need something funny"],
        "ai": [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "I told my computer I needed a break, and now it won’t stop sending me KitKats.",
            "Why did the math book look sad? Because it had too many problems.",
            "Why do cows have hooves instead of feet? Because they lactose."
        ]
    },
    "advice": {
        "user": ["I need some advice", "Can you help me with a problem?", "What should I do?", "I'm feeling stuck", "Give me life advice"],
        "ai": [
            "The best way to solve a problem is to break it into smaller, manageable steps. What's on your mind?",
            "Sometimes, taking a break can give you a new perspective. What are you stuck on?",
            "Trust your instincts and take things one step at a time. Is there something specific you need help with?",
            "When feeling stuck, try talking to someone or changing your environment. It can really help!",
            "Life is about progress, not perfection. Focus on taking small steps forward."
        ]
    },
    "tech_support": {
        "user": ["My computer is slow", "Can you fix my phone?", "How do I install software?", "My internet is not working", "I forgot my password"],
        "ai": [
            "Try restarting your computer and checking for updates. That often helps with slow performance.",
            "I can't fix your phone directly, but restarting it or updating the software may help.",
            "You can install software by downloading it from the official website and following the instructions.",
            "Make sure your router is plugged in and try restarting it. If that doesn’t work, contact your ISP.",
            "You can reset your password using the 'Forgot Password' option on the login page."
        ]
    },
    "productivity": {
        "user": ["How can I be more productive?", "I need tips for staying focused", "How do I manage my time?", "I'm procrastinating"],
        "ai": [
            "Try using the Pomodoro technique: work for 25 minutes, then take a 5-minute break.",
            "Staying focused is easier if you eliminate distractions and set clear goals.",
            "Prioritize your tasks and tackle the most important ones first. Time management is key.",
            "Breaking tasks into smaller steps can help you overcome procrastination. Start small."
        ]
    },
    "food_and_recipes": {
        "user": ["What's a good recipe for dinner?", "What should I cook?", "Do you have a simple meal idea?", "I need a quick snack"],
        "ai": [
            "How about pasta with marinara sauce? It's quick and delicious!",
            "You could make a stir-fry with veggies, chicken, and some soy sauce. Healthy and fast!",
            "A simple grilled cheese sandwich always works for a quick meal.",
            "Try making popcorn or a peanut butter and banana sandwich for a fast snack!"
        ]
    },
    "health_and_wellness": {
        "user": ["How can I stay healthy?", "Any fitness tips?", "How do I manage stress?", "What should I eat?", "How much water should I drink?"],
        "ai": [
            "Staying healthy is about balance. Eat well, stay active, and get enough rest.",
            "For fitness, try a mix of cardio and strength exercises. Even a daily walk makes a difference!",
            "Managing stress is important. Deep breathing, meditation, and regular exercise can help.",
            "A balanced diet with fruits, veggies, and protein is key to staying healthy.",
            "It’s recommended to drink about 8 glasses of water a day, but it depends on your activity level."
        ]
    },
    "miscellaneous": {
        "user": ["What is your favorite color?", "Do you like music?", "Can you dance?", "What’s the meaning of life?", "Tell me something interesting"],
        "ai": [
            "I don’t have a favorite color, but blue seems to be popular!",
            "I can't listen to music, but I know a lot about it. What's your favorite genre?",
            "I don’t have legs, so dancing is a bit tricky for me!",
            "Philosophers have debated the meaning of life for centuries. Many believe it's about happiness and purpose.",
            "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!"
        ]
    },
        "1": {
        "user": "I'm feeling really stressed with my studies. I don't know how to manage everything.",
        "chatbot": "I'm sorry to hear that you're feeling this way. It's okay to feel overwhelmed at times. Can you share what's causing the most stress for you?"
    },
    "2": {
        "user": "I have so many assignments and exams coming up, and I'm not sure I can handle it all.",
        "chatbot": "That sounds tough, but remember, you're capable of more than you think. Have you tried breaking down the tasks into smaller, more manageable pieces?"
    },
    "3": {
        "user": "I don't even know where to start. It feels like too much.",
        "chatbot": "It's understandable to feel lost when things pile up. Let's start by prioritizing. What’s the most urgent assignment or exam that you need to focus on right now?"
    },
    "4": {
        "user": "I have an assignment due tomorrow, but I also have to prepare for an exam next week.",
        "chatbot": "Let’s focus on the assignment for now, as it's due sooner. Once you make some progress, you'll feel more in control, and then you can plan for your exam. Would you like help with structuring your time?"
    },
    "5": {
        "user": "Yes, I think that would help.",
        "chatbot": "Great! How about setting a 25-minute timer to work on the assignment, then taking a 5-minute break? You can repeat this a few times and check your progress after."
    },
    "6": {
        "user": "Okay, I’ll try that.",
        "chatbot": "You’re doing great! Remember, it's okay to take things one step at a time. If you need to talk or need more help organizing, I’m here for you."
    },
    "7": {
        "user": "Thanks. I feel a bit better now.",
        "chatbot": "I'm glad to hear that! It's important to take care of yourself during stressful times. If you ever feel overwhelmed again, don't hesitate to reach out. You're not alone in this."
    },
        "stress": {
            "1": {
                "user": "I'm feeling really stressed with my studies.",
                "chatbot": "I'm sorry you're feeling this way. Can you share what’s causing you the most stress right now?"
            },
            "2": {
                "user": "I don't have enough time for my assignments.",
                "chatbot": "Time management can be tough. Have you tried breaking your tasks into smaller, more manageable steps?"
            },
            "3": {
                "user": "I just have too much work to do.",
                "chatbot": "That sounds overwhelming. How about focusing on one task at a time? Start with the most urgent one."
            },
            "4": {
                "user": "I'm worried about not meeting deadlines.",
                "chatbot": "It’s natural to worry about deadlines. Have you considered creating a timeline or schedule to help you stay on track?"
            }
        },
        "anxiety": {
            "1": {
                "user": "I feel really anxious before exams.",
                "chatbot": "Exam anxiety is quite common. How do you usually prepare for your exams?"
            },
            "2": {
                "user": "I feel like I'm going to fail.",
                "chatbot": "It’s normal to feel anxious, but remember you’ve studied and prepared. You can only do your best."
            },
            "3": {
                "user": "I can’t focus because I’m so nervous.",
                "chatbot": "When you’re nervous, it can be hard to focus. Have you tried deep breathing exercises or taking short breaks to clear your mind?"
            },
            "4": {
                "user": "I feel overwhelmed with everything.",
                "chatbot": "Feeling overwhelmed is tough. It’s okay to take a step back. Let’s break things down and tackle one task at a time."
            }
        },
        "loneliness": {
            "1": {
                "user": "I feel really lonely. I don’t have anyone to talk to.",
                "chatbot": "I’m really sorry you feel that way. It’s important to know that you're not alone, and I’m here for you."
            },
            "2": {
                "user": "I don’t have friends at college. It makes me feel isolated.",
                "chatbot": "Making new friends can be hard. Have you tried joining any student clubs or study groups to meet new people?"
            },
            "3": {
                "user": "I don’t feel like anyone understands me.",
                "chatbot": "That can be really difficult. Sometimes talking about how you feel can help. I’m here to listen if you want to share more."
            },
            "4": {
                "user": "I don’t even feel like going out anymore.",
                "chatbot": "It sounds like you’re feeling down. Sometimes, getting out for a short walk or calling someone you trust can help you feel a little better."
            }
        },
        "motivation_issues": {
            "1": {
                "user": "I can’t seem to find the motivation to study.",
                "chatbot": "It’s okay to feel unmotivated at times. Is there something specific that’s making studying hard for you right now?"
            },
            "2": {
                "user": "I’m just so tired of everything.",
                "chatbot": "It sounds like you might need a break. Rest is important too. How about taking a short break and then coming back to your studies with a fresh mind?"
            },
            "3": {
                "user": "I keep procrastinating and falling behind.",
                "chatbot": "Procrastination can be tough to manage. How about setting small, achievable goals and rewarding yourself after completing each one?"
            },
            "4": {
                "user": "I just don’t care anymore about my studies.",
                "chatbot": "It sounds like you're feeling really down. Sometimes when we lose interest, it can help to reconnect with why we started in the first place. What originally motivated you to pursue your studies?"
            }
        },
        "self_doubt": {
            "1": {
                "user": "I don’t think I’m good enough for this course.",
                "chatbot": "It’s common to doubt yourself, but remember, you’re here for a reason. You’re capable of more than you might realize."
            },
            "2": {
                "user": "I feel like everyone else is doing better than me.",
                "chatbot": "Comparing yourself to others can be discouraging. Focus on your own progress—you’re moving at your own pace, and that’s okay."
            },
            "3": {
                "user": "What if I fail? I’m not sure I can handle it.",
                "chatbot": "It’s natural to fear failure, but remember, failing is part of learning. What’s important is that you keep trying and learning from any mistakes."
            },
            "4": {
                "user": "I just don’t think I’m smart enough.",
                "chatbot": "You’re smarter than you think. Intelligence isn’t just about knowing everything—it’s about being willing to learn and grow, and you’re doing that."
            }
        },
        "general_support": {
            "1": {
                "user": "I’m having a really tough day.",
                "chatbot": "I’m sorry to hear that. Do you want to talk about what’s going on? I’m here to listen."
            },
            "2": {
                "user": "I just feel sad for no reason.",
                "chatbot": "It’s okay to feel sad sometimes, even if you can’t pinpoint why. What can you do today to take care of yourself?"
            },
            "3": {
                "user": "I don’t feel like doing anything.",
                "chatbot": "That’s okay. It’s important to give yourself permission to rest when you’re feeling low. Maybe a small, gentle activity could help lift your mood?"
            },
            "4": {
                "user": "Everything just feels too hard right now.",
                "chatbot": "I’m really sorry things feel so hard. You don’t have to do everything at once. What’s one small thing you can do today to take care of yourself?"
            }
        },
        "self_care_tips": {
            "1": {
                "user": "How can I take care of my mental health?",
                "chatbot": "Taking care of your mental health can include regular breaks, talking to friends, exercising, and practicing mindfulness or meditation. Do you already do any of these?"
            },
            "2": {
                "user": "What are some ways to reduce stress?",
                "chatbot": "Stress management can include deep breathing exercises, staying organized, getting enough sleep, and doing activities you enjoy. Have you tried any of these before?"
            },
            "3": {
                "user": "How do I stay positive when things are tough?",
                "chatbot": "Staying positive during tough times can be challenging. Try practicing gratitude, focusing on what you can control, and seeking support from friends or family."
            },
            "4": {
                "user": "What should I do when I feel overwhelmed?",
                "chatbot": "When feeling overwhelmed, try to take a step back and breathe. Break tasks into smaller steps, and prioritize what’s most important. You can also talk to someone for support."
            }
        },
            "burnout": {
                "1": {
                    "user": "I feel completely burnt out. I can’t focus anymore.",
                    "chatbot": "Burnout is a sign that you’ve been pushing yourself too hard. It’s important to take breaks and rest. Have you considered taking a day off to recharge?"
                },
                "2": {
                    "user": "I’m so exhausted, but I feel guilty when I’m not studying.",
                    "chatbot": "It’s understandable to feel that way, but rest is just as important as work. You can’t perform your best when you’re running on empty. Taking time to rest will help you be more productive later."
                },
                "3": {
                    "user": "I don’t have the energy to keep going, but I have so much to do.",
                    "chatbot": "When you feel drained, it’s okay to step back. Try focusing on one small task at a time, and give yourself permission to rest afterward. You’ll come back stronger."
                },
                "4": {
                    "user": "I don’t enjoy studying anymore. It feels like a chore.",
                    "chatbot": "When studying becomes a chore, it could be a sign of burnout. Maybe switch up your study routine or find something you enjoy to break the monotony. What’s one thing you could do for fun today?"
                }
            },
            "perfectionism": {
                "1": {
                    "user": "I can’t stop worrying about making mistakes in my work.",
                    "chatbot": "It’s normal to want to do your best, but remember that mistakes are part of learning. Have you tried setting realistic expectations for yourself?"
                },
                "2": {
                    "user": "I keep redoing my work because it’s never good enough.",
                    "chatbot": "Perfectionism can be exhausting. Sometimes it helps to remind yourself that good enough is still progress. Have you tried setting a time limit for each task to avoid overworking it?"
                },
                "3": {
                    "user": "I’m afraid people will judge me if my work isn’t perfect.",
                    "chatbot": "It’s natural to worry about what others think, but often we are our own toughest critics. What if you focused more on learning and improving, rather than on perfection?"
                },
                "4": {
                    "user": "I feel like I’m never doing enough.",
                    "chatbot": "You’re doing your best, and that’s enough. It’s important to acknowledge your efforts and progress, even if things aren’t perfect. How about celebrating a small win today?"
                }
            },
            "social_anxiety": {
                "1": {
                    "user": "I get really nervous when I have to speak in class.",
                    "chatbot": "Speaking in front of others can be nerve-wracking, but remember that your voice matters. Could you try preparing a few notes or practicing with a friend to feel more confident?"
                },
                "2": {
                    "user": "I’m scared people will judge me if I say something wrong.",
                    "chatbot": "It’s understandable to feel that way, but everyone makes mistakes, and it’s a part of learning. Most people are focused on their own thoughts, not on judging others. Could that help ease your worry?"
                },
                "3": {
                    "user": "I always overthink my interactions with others.",
                    "chatbot": "Overthinking can be exhausting. Try reminding yourself that most people aren’t analyzing you as much as you think. How about focusing on how the conversation made you feel instead of over-analyzing it?"
                },
                "4": {
                    "user": "I avoid social situations because I get too anxious.",
                    "chatbot": "Social anxiety can be difficult. It’s okay to take small steps, like attending a casual event or meeting one person at a time. Would you like tips for managing anxiety in social situations?"
                }
            },
            "imposter_syndrome": {
                "1": {
                    "user": "I feel like I don’t deserve to be here. Everyone else seems smarter than me.",
                    "chatbot": "Imposter syndrome can be tough, but remember, you’ve earned your place here just like everyone else. Have you thought about writing down your achievements to remind yourself of how far you’ve come?"
                },
                "2": {
                    "user": "I’m worried people will find out I’m not as capable as they think.",
                    "chatbot": "Many people experience imposter syndrome, but it doesn’t reflect reality. You’re more capable than you give yourself credit for. What’s one thing you’ve done recently that you’re proud of?"
                },
                "3": {
                    "user": "I don’t feel like I belong in my course.",
                    "chatbot": "It’s normal to feel out of place sometimes, but remember, you’ve been chosen for a reason. You have skills and talents to contribute. Have you reached out to classmates or mentors for support?"
                },
                "4": {
                    "user": "No matter what I achieve, it never feels like enough.",
                    "chatbot": "It’s hard when nothing feels like enough. Have you tried celebrating even the small wins? Recognizing your progress can help build your confidence over time."
                }
            },
            "relationship_issues": {
                "1": {
                    "user": "I’m having trouble with my friends. We’ve been arguing a lot lately.",
                    "chatbot": "Friendship challenges can be really tough. Have you talked to your friends about how you’re feeling? Open communication can help clear misunderstandings."
                },
                "2": {
                    "user": "I feel like my friends don’t understand me anymore.",
                    "chatbot": "Sometimes people grow in different directions, and that’s okay. Have you tried sharing how you’re feeling with them to see if they might be more understanding?"
                },
                "3": {
                    "user": "I’m afraid of losing my friends if I don’t keep up with them.",
                    "chatbot": "It’s normal to worry about friendships, but true friends will understand if you need space sometimes. Have you considered setting boundaries or finding a balance that works for you?"
                },
                "4": {
                    "user": "I’m feeling really distant from my family lately.",
                    "chatbot": "Feeling distant from family can be difficult. Maybe reaching out for a small conversation or shared activity could help bridge the gap. Would that be something you’d like to try?"
                }
            },
            "dealing_with_failure": {
                "1": {
                    "user": "I failed my exam, and I feel like a failure.",
                    "chatbot": "I’m really sorry you’re feeling this way. Failing an exam doesn’t define your worth or abilities. It’s an opportunity to learn and improve. What do you think went wrong, and how can we work on it?"
                },
                "2": {
                    "user": "I feel like I’ll never succeed at anything.",
                    "chatbot": "It’s understandable to feel this way after a setback, but remember that failure is a stepping stone to success. Everyone experiences failures, and they don’t diminish your potential."
                },
                "3": {
                    "user": "I let everyone down by failing this test.",
                    "chatbot": "It’s easy to feel like you’ve disappointed others, but your worth isn’t based on one test. Have you considered talking to someone about how you’re feeling? They may not see it the way you do."
                },
                "4": {
                    "user": "What’s the point in trying if I keep failing?",
                    "chatbot": "It’s hard to stay motivated after failure, but remember, persistence is key. Every attempt is progress. Let’s figure out what can be done differently next time."
                }
            },
            "self_compassion": {
                "1": {
                    "user": "I’m really hard on myself when I don’t do well.",
                    "chatbot": "It’s common to be your own toughest critic, but self-compassion is important. How about practicing some kindness toward yourself? You’re doing your best, and that’s what matters."
                },
                "2": {
                    "user": "I always feel guilty for taking breaks.",
                    "chatbot": "Rest is a crucial part of productivity. You deserve breaks, and they help you recharge. Try reminding yourself that taking time to rest will help you do better in the long run."
                },
                "3": {
                    "user": "I’m not good at giving myself credit for my achievements.",
                    "chatbot": "Acknowledging your achievements is important for self-confidence. Even small wins are worth celebrating. How about writing down one thing you’re proud of today?"
                },
                "4": {
                    "user": "I feel like I’m never good enough.",
                    "chatbot": "You are enough just as you are. It’s important to recognize your unique strengths and efforts. No one is perfect, but you are valuable and capable."
                }
            },
    "procrastination": {
        "1": {
            "user": "I keep putting off my assignments, and now I’m behind.",
            "chatbot": "Procrastination can be a tough cycle to break. Try setting small, specific goals to start with, and reward yourself for completing each one."
        },
        "2": {
            "user": "I always say I’ll start studying tomorrow, but I never do.",
            "chatbot": "That’s a common problem. How about starting with just 5 minutes of work right now? Sometimes getting started is the hardest part."
        },
        "3": {
            "user": "I just keep finding excuses to not do my work.",
            "chatbot": "It’s easy to get distracted, but remember why you started. What’s one small thing you can do right now to get back on track?"
        },
        "4": {
            "user": "I’m overwhelmed by how much I have to do, so I avoid it.",
            "chatbot": "When everything feels like too much, try breaking tasks into smaller pieces. Focus on one step at a time, and it will feel more manageable."
        }
    },
    "depression": {
        "1": {
            "user": "I feel so low that I can’t get out of bed.",
            "chatbot": "I’m really sorry you’re feeling this way. It’s important to take things one step at a time. Even just getting up and moving around a little can help."
        },
        "2": {
            "user": "I don’t feel like doing anything, not even things I used to enjoy.",
            "chatbot": "That can be really tough. It might help to start with something small and easy. Doing even one little thing can sometimes lift your mood."
        },
        "3": {
            "user": "I feel like I’m stuck in a dark place and can’t get out.",
            "chatbot": "It sounds like you’re going through a really difficult time. Remember that you don’t have to go through this alone—reaching out to someone you trust can make a difference."
        },
        "4": {
            "user": "Nothing seems to make me happy anymore.",
            "chatbot": "That sounds really hard. Sometimes, trying something new or getting a change of scenery can help. Have you talked to anyone about how you’re feeling?"
        }
    },
    "handling_rejection": {
        "1": {
            "user": "I got rejected from the internship I applied for, and now I feel hopeless.",
            "chatbot": "Rejection is always hard, but it’s part of the process. It doesn’t define your abilities or worth. What did you learn from this experience that you can use next time?"
        },
        "2": {
            "user": "I didn’t get the grade I wanted, and now I feel like I’ll never succeed.",
            "chatbot": "It’s okay to feel disappointed, but remember that one grade doesn’t define your future. What can you do differently to prepare for the next exam?"
        },
        "3": {
            "user": "My friends rejected me, and now I feel like something’s wrong with me.",
            "chatbot": "I’m really sorry you’re feeling this way. Sometimes friendships change, and it’s not always about you. It might help to talk to them about what’s going on."
        },
        "4": {
            "user": "I keep getting rejected from everything I try for.",
            "chatbot": "Rejection can feel discouraging, but every ‘no’ brings you closer to a ‘yes.’ It’s a numbers game, and persistence is key."
        }
    },
    "fear_of_the_future": {
        "1": {
            "user": "I’m scared I won’t succeed in my career.",
            "chatbot": "It’s natural to feel uncertain about the future, but remember that success is a journey. Focus on what you can do now to build toward your goals."
        },
        "2": {
            "user": "I don’t know what I want to do with my life, and it worries me.",
            "chatbot": "It’s okay to not have everything figured out yet. Many people take time to discover their path. What are some things you enjoy or are curious about?"
        },
        "3": {
            "user": "I’m afraid of failing after I graduate.",
            "chatbot": "Graduation can bring a lot of uncertainty, but it’s also a time for new opportunities. What steps can you take to prepare for the transition?"
        },
        "4": {
            "user": "The future seems so overwhelming and uncertain.",
            "chatbot": "It’s understandable to feel overwhelmed. Try focusing on what you can control, and take things one step at a time. What’s something small you can do today?"
        }
    },
    "self-worth": {
        "1": {
            "user": "I don’t feel like I’m good at anything.",
            "chatbot": "It’s easy to feel down on yourself, but everyone has strengths. What’s something you’ve done recently that made you feel proud, no matter how small?"
        },
        "2": {
            "user": "I feel like no one appreciates me.",
            "chatbot": "Feeling unappreciated can be really hard. Sometimes people don’t express gratitude enough, but that doesn’t mean you aren’t valued. Have you thought about sharing how you feel with someone close to you?"
        },
        "3": {
            "user": "I don’t think I’m worth much compared to others.",
            "chatbot": "It’s easy to compare yourself to others, but your value isn’t based on comparison. You have unique strengths and qualities that make you valuable."
        },
        "4": {
            "user": "I don’t believe in myself anymore.",
            "chatbot": "I’m really sorry you’re feeling this way. Belief in yourself can come and go, but it’s important to recognize that you’ve overcome challenges before. What’s something you’ve accomplished that you’re proud of?"
        }
    },
    "handling_criticism": {
        "1": {
            "user": "I can’t stop thinking about the negative feedback I got.",
            "chatbot": "Criticism can be tough to handle, but it’s also an opportunity to grow. What part of the feedback can you use to improve next time?"
        },
        "2": {
            "user": "I always take criticism personally, and it really hurts.",
            "chatbot": "It’s understandable to feel hurt, but try to remember that feedback is about improving, not a reflection of your worth. How can you use it constructively?"
        },
        "3": {
            "user": "I feel like people are always criticizing me.",
            "chatbot": "Constant criticism can feel overwhelming. It might help to take a step back and decide which feedback is helpful and which isn’t. How do you usually respond to criticism?"
        },
        "4": {
            "user": "I’m afraid to try new things because of fear of criticism.",
            "chatbot": "Fear of criticism is common, but remember that mistakes are part of learning. What’s something you’d like to try, even if it’s just a small step?"
        }
    },
    "finding_balance": {
        "1": {
            "user": "I feel like I’m always working and never have time for myself.",
            "chatbot": "Finding balance is important for your well-being. Can you schedule some time for self-care or something you enjoy each day?"
        },
        "2": {
            "user": "I feel guilty when I take breaks.",
            "chatbot": "Breaks are necessary for productivity and mental health. You deserve to rest, and it will help you come back stronger. Try reminding yourself that breaks are part of the process."
        },
        "3": {
            "user": "I’m struggling to balance my studies with my social life.",
            "chatbot": "Balancing social life and studies can be tricky. Have you tried setting boundaries, like dedicating specific time for both?"
        },
        "4": {
            "user": "I don’t know how to make time for everything I want to do.",
            "chatbot": "It can help to prioritize and focus on what’s most important to you. Maybe start by identifying your top priorities and allocating time for them."
        }
    },
    "managing_expectations": {
        "1": {
            "user": "I feel like everyone expects too much from me.",
            "chatbot": "It’s hard when expectations feel overwhelming. It might help to set boundaries and communicate your limits with others. You can’t do everything at once, and that’s okay."
        },
        "2": {
            "user": "I’m afraid I’ll let people down if I don’t meet their expectations.",
            "chatbot": "It’s natural to feel pressure from others, but remember that your well-being comes first. What expectations are you feeling most pressured by right now?"
        },    

            "anxiety": {
                "I feel so anxious all the time.": "I'm sorry you're feeling this way. Remember, anxiety can be overwhelming, but you're not alone in this. Taking slow, deep breaths might help you feel calmer in this moment.",
                "My anxiety is making it hard to focus.": "That sounds really tough. When anxiety gets overwhelming, it can affect your concentration. Taking a short break or doing something that grounds you could help reset your mind.",
                "I can't stop worrying about everything.": "It's exhausting when worries take over. It might help to write down your thoughts or talk to someone you trust about how you're feeling.",
            },
            "depression": {
                "I feel like I’m not good enough.": "I'm really sorry you're feeling this way, but you are important, and your feelings are valid. Please be kind to yourself, and remember that reaching out for support can make a difference.",
                "I don't feel motivated to do anything anymore.": "It's okay to not feel motivated sometimes, especially when you're going through a difficult time. Small steps, even just getting out of bed, are still progress.",
                "Everything just feels hopeless.": "I'm really sorry you're feeling like this. Sometimes it can feel like there's no way out, but things can get better. Reaching out to a friend or professional could help you find some support.",
            },
            "stress": {
                "I'm overwhelmed with everything happening right now.": "It sounds like you're carrying a lot right now. Taking things one step at a time or prioritizing tasks might help ease the weight. Remember to breathe and give yourself a moment to pause.",
                "I can't handle all this stress.": "I'm really sorry you're feeling this way. It can be helpful to talk through what's causing your stress or take a break to recharge. Self-care is important, especially when you're feeling overwhelmed.",
                "I feel like I'm on the verge of burnout.": "It sounds like you've been pushing yourself really hard. Taking some time to rest and prioritize your well-being can help prevent burnout. It's okay to ask for help when you need it.",
            },
            "self-worth": {
                "I don't feel like I matter.": "I'm really sorry you're feeling this way. You do matter, and your presence in this world makes a difference. Sometimes it helps to talk to someone who can remind you of your worth.",
                "I keep comparing myself to others.": "Comparing yourself to others can be really discouraging. Everyone has their own journey, and your path is unique. Try focusing on your own progress and the things that make you proud.",
                "I feel like I'm not enough.": "It’s hard when you feel like that, but you are enough just as you are. Try to be gentle with yourself, and remember that worth isn't determined by what you achieve, but by who you are.",
            },
            "fear_of_failure": {
                "I'm scared of failing at this.": "It’s okay to be afraid of failure, but remember that failure is often part of growth. Even if things don’t go as planned, you’ll learn and come out stronger.",
                "What if I fail and disappoint everyone?": "I understand that fear, but remember that your worth isn't defined by success or failure. The people who care about you will support you no matter what.",
                "I feel paralyzed by the fear of not succeeding.": "Fear can be so powerful, but taking small steps forward can help ease that feeling. It’s okay to feel scared, but you don’t have to face it alone. You can always reach out for support.",
            },
            "loneliness": {
                "I feel so alone, like no one understands me.": "I’m really sorry you’re feeling alone right now. Even if it feels like no one understands, there are people who care about you. Sometimes reaching out can help make things feel a little lighter.",
                "I don't have anyone to talk to.": "That sounds incredibly tough. Feeling disconnected is painful, but you’re not alone. If you're comfortable, maybe trying to connect with a support group or someone you trust could help.",
                "I feel invisible to everyone around me.": "It’s really hard to feel like no one sees you. You are important and deserve to be heard. Talking to someone who cares might help you feel more seen.",
            },
            "grief": {
                "I miss them so much, I don’t know how to move on.": "Grief is so difficult, and missing someone you’ve lost can feel overwhelming. It’s okay to take your time. Healing doesn’t have a timeline, and it's okay to feel how you’re feeling.",
                "I can’t stop thinking about them, it’s consuming me.": "Grief can take over everything. It’s okay to feel this way and to take time to process your feelings. Talking to someone who understands might help you carry this load.",
                "I don’t know if I’ll ever feel better again.": "It’s okay to feel this way right now. Grief can feel like it will never end, but with time and support, the pain can become more bearable. You don’t have to go through it alone."
            },

                "excitement": {
                    "I'm so excited about the weekend!": "That's awesome! Having something fun to look forward to can really brighten the week. Do you have any special plans?",
                    "I can't wait for the party tonight!": "That sounds like it's going to be a great time! I hope you enjoy every moment.",
                    "I'm excited but also a little nervous.": "It’s normal to feel a mix of excitement and nerves! Just focus on the fun, and things will fall into place."
                },
                "party": {
                    "I'm going to a party later!": "That’s great! I hope you have an amazing time. Parties can be a lot of fun, especially when you're with good company.",
                    "What should I wear to the party?": "It depends on the vibe! If it's casual, go for something comfortable but stylish. If it's fancy, maybe a little more dressed up. What's the occasion?",
                    "I'm worried I won't know anyone at the party.": "It can be tough going to a party where you don’t know many people. Maybe start by chatting with the host or someone you know a little. You never know who you might meet!"
                },
                "dress": {
                    "What should I wear to the event?": "Think about the event's vibe—casual or formal? Go with something that makes you feel confident and comfortable. If you're unsure, a classic look is always a safe bet.",
                    "I love this dress I bought!": "That’s awesome! Feeling great in what you wear can really boost your confidence. How do you feel in it?",
                    "Does this outfit look okay?": "It sounds like you want to feel your best. If you feel good in it, that’s what really matters! But if you're unsure, maybe try a quick mirror check or ask a friend for their opinion."
                },
                "dress_code": {
                    "What's the dress code for the event?": "It’s always a good idea to double-check the invite! If it says formal, go fancy. If it's casual, something more laid back should work. Do you know what others might be wearing?",
                    "Should I dress formally for this event?": "If you're unsure, it’s better to be slightly overdressed than underdressed. You can always adjust based on what the event feels like when you get there.",
                    "I'm worried I'll stand out because of my outfit.": "It’s natural to feel that way sometimes. But remember, confidence makes any outfit look good. As long as you’re comfortable, that’s what counts!"
                },
                "functions": {
                    "I'm going to a wedding this weekend.": "How exciting! Weddings are such a special celebration. I hope you have a wonderful time celebrating with the couple.",
                    "I have to attend a formal event tonight.": "That sounds like it could be fun! Just enjoy the experience and make sure to wear something that makes you feel confident.",
                    "What's the best way to prepare for a big function?": "Getting ready early always helps! Make sure you’ve got your outfit sorted and give yourself some time to relax beforehand. It’ll help you feel more at ease when you get there."
                },
                "dance": {
                    "I love dancing at parties!": "That’s amazing! Dancing is such a fun way to express yourself and let loose. What kind of music do you like dancing to?",
                    "I’m nervous about dancing in front of others.": "It’s completely normal to feel that way! Try focusing on the music and having fun—people are usually too busy dancing themselves to notice too much.",
                    "What’s your favorite dance style?": "I think all kinds of dance are great! Whether it's something upbeat like salsa or something relaxed like a slow dance, it's all about the joy of moving to the music."
                },
                "songs": {
                    "Do you have any song recommendations?": "Sure! It depends on what you're in the mood for. If you’re feeling upbeat, maybe something with a great beat like pop or electronic. If you’re in a mellow mood, maybe some indie or acoustic tunes.",
                    "I can't get this song out of my head!": "That happens sometimes! It must be a catchy one. Maybe creating a playlist of similar songs could keep the good vibes going.",
                    "What kind of music do you like?": "I like all sorts of music! Whether it’s for dancing, relaxing, or getting in the zone, there’s a song for every moment."
                },
                "martial_arts": {
                    "I'm thinking about starting martial arts.": "That sounds like an amazing idea! Martial arts can be great for both physical fitness and mental discipline. Do you know which style you'd like to try?",
                    "I have a martial arts class today!": "That’s exciting! Martial",
                },
    }

}

