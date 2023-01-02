from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.Inicio, name="Inicio"),
    path('cursos/', views.Cursos, name="Cursos"),
    path('cursos/lista/', views.VerCursos, name="CursosLista"),
    path('cursosApi/', views.Cursosapi),
    path("profesor/",views.Profesores, name="Profesor"),
    path("alumnos/",views.Alumnos, name="Alumnos"),
    path("buscar/",views.Buscar, name="Buscar"),
    path("buscarcurso/",views.buscarcurso, name="Buscarc"),
    # path("leercursos/",views.leer_curso, name="Leer Curso"),
    # path("crearcursos/",views.crear_curso, name="Crear Curso"),
    # path("editarcursos/",views.editar_curso, name="Editar Curso"),
    # path("eliminarcursos/",views.eliminar_curso, name="Eliminar Curso"),
    path('curso/list/', views.CursoList.as_view(), name ="List"),
    path("curso/create/", views.CursoCreate.as_view(), name="New"),
    path("curso/edit/<pk>", views.CursoEdit.as_view(), name="Edit"),
    path("curso/detail/<pk>", views.CursoDetail.as_view(), name="Detail"),
    path("curso/delete/<pk>", views.CursoDelete.as_view(), name="Delete")
]