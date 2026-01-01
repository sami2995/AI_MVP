from django.shortcuts import render, get_object_or_404
from .models import Subject, Topic, Material, Quiz, QuizResult


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})


def topic_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    topics = Topic.objects.filter(subject=subject)
    return render(request, 'topic_list.html', {
        'subject': subject,
        'topics': topics
    })


def material_list(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    materials = Material.objects.filter(topic=topic)
    quizzes = Quiz.objects.filter(topic=topic)

    return render(request, 'material_list.html', {
        'topic': topic,
        'materials': materials,
        'quizzes': quizzes
    })


def quiz_results(request):
    results = QuizResult.objects.filter(user=request.user)
    return render(request, 'quiz_results.html', {'results': results})


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    # load questions and choices
    questions = []
    for q in quiz.question_set.all():
        choices = q.choice_set.all()
        questions.append({'question': q, 'choices': choices})

    return render(request, 'quiz_detail.html', {
        'quiz': quiz,
        'questions': questions,
    })
