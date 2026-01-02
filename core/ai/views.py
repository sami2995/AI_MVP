from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject, Topic, Material, Quiz, QuizResult


def subject_list(request):
    subjects = Subject.objects.filter(visible=True)
    # Add statistics
    stats = {
        'total_subjects': subjects.count(),
        'total_topics': Topic.objects.filter(visible=True).count(),
        'total_materials': Material.objects.filter(visible=True).count(),
        'total_quizzes': Quiz.objects.filter(visible=True).count(),
    }
    return render(request, 'subjects.html', {'subjects': subjects, 'stats': stats})


def topic_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    topics = Topic.objects.filter(subject=subject, visible=True)
    # Add statistics
    stats = {
        'total_topics': topics.count(),
        'total_materials': Material.objects.filter(topic__subject=subject, visible=True).count(),
        'total_quizzes': Quiz.objects.filter(topic__subject=subject, visible=True).count(),
    }
    return render(request, 'topic_list.html', {
        'subject': subject,
        'topics': topics,
        'stats': stats
    })


def material_list(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    materials = Material.objects.filter(topic=topic, visible=True)
    quizzes = Quiz.objects.filter(topic=topic, visible=True)
    
    # Add statistics
    stats = {
        'total_materials': materials.count(),
        'total_quizzes': quizzes.count(),
    }

    return render(request, 'material_list.html', {
        'topic': topic,
        'materials': materials,
        'quizzes': quizzes,
        'stats': stats
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


# ========== SUBJECT CRUD ==========
def subject_admin(request):
    subjects = Subject.objects.filter(visible=True)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')
        obj = Subject()
        obj.name = name
        obj.description = description
        obj.image = image
        obj.save()
    return render(request, 'subject_admin.html', {'subjects': subjects})


def subject_edit(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')
        subject.name = name
        subject.description = description
        subject.image = image if image is not None else subject.image
        subject.save()
        return redirect('subject_admin_url')
    return render(request, 'edit_subject.html', {'subject': subject})


def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    subject.visible = False
    subject.save()
    return redirect('subject_admin_url')


# ========== TOPIC CRUD ==========
def topic_admin(request):
    topics = Topic.objects.filter(visible=True)
    subjects = Subject.objects.filter(visible=True)
    if request.method == 'POST':
        title = request.POST.get('title')
        subject_id = request.POST.get('subject')
        obj = Topic()
        obj.title = title
        obj.subject = Subject.objects.get(id=subject_id)
        obj.save()
    return render(request, 'topic_admin.html', {'topics': topics, 'subjects': subjects})


def topic_edit(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    subjects = Subject.objects.filter(visible=True)
    if request.method == 'POST':
        title = request.POST.get('title')
        subject_id = request.POST.get('subject')
        topic.title = title
        topic.subject = Subject.objects.get(id=subject_id)
        topic.save()
        return redirect('topic_admin_url')
    return render(request, 'edit_topic.html', {'topic': topic, 'subjects': subjects})


def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    topic.visible = False
    topic.save()
    return redirect('topic_admin_url')


# ========== MATERIAL CRUD ==========
def material_admin(request):
    materials = Material.objects.filter(visible=True)
    topics = Topic.objects.filter(visible=True)
    if request.method == 'POST':
        topic_id = request.POST.get('topic')
        file = request.FILES.get('file')
        obj = Material()
        obj.topic = Topic.objects.get(id=topic_id)
        obj.file = file
        obj.save()
    return render(request, 'material_admin.html', {'materials': materials, 'topics': topics})


def material_edit(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    topics = Topic.objects.filter(visible=True)
    if request.method == 'POST':
        topic_id = request.POST.get('topic')
        file = request.FILES.get('file')
        material.topic = Topic.objects.get(id=topic_id)
        material.file = file if file is not None else material.file
        material.save()
        return redirect('material_admin_url')
    return render(request, 'edit_material.html', {'material': material, 'topics': topics})


def delete_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    material.visible = False
    material.save()
    return redirect('material_admin_url')


# ========== QUIZ CRUD ==========
def quiz_admin(request):
    quizzes = Quiz.objects.filter(visible=True)
    topics = Topic.objects.filter(visible=True)
    if request.method == 'POST':
        title = request.POST.get('title')
        topic_id = request.POST.get('topic')
        obj = Quiz()
        obj.title = title
        obj.topic = Topic.objects.get(id=topic_id)
        obj.save()
    return render(request, 'quiz_admin.html', {'quizzes': quizzes, 'topics': topics})


def quiz_edit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    topics = Topic.objects.filter(visible=True)
    if request.method == 'POST':
        title = request.POST.get('title')
        topic_id = request.POST.get('topic')
        quiz.title = title
        quiz.topic = Topic.objects.get(id=topic_id)
        quiz.save()
        return redirect('quiz_admin_url')
    return render(request, 'edit_quiz.html', {'quiz': quiz, 'topics': topics})


def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.visible = False
    quiz.save()
    return redirect('quiz_admin_url')
