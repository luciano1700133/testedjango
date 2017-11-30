from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'app.views.pagina_inicial', name='pagina_inicial'),

    url(r'^listar_aluno', 'app.views.listar_aluno', name='listar_aluno'),
    url(r'^novo_aluno', 'app.views.novo_aluno', name='novo_aluno'),
    url(r'^editar_aluno/(?P<pk>\d+)$', 'app.views.editar_aluno', name='editar_aluno'),
    url(r'^apagar_aluno/(?P<pk>\d+)$', 'app.views.apagar_aluno', name='apagar_aluno'),

    url(r'^listar_curso', 'app.views.listar_curso', name='listar_curso'),
    url(r'^novo_curso', 'app.views.novo_curso', name='novo_curso'),
    url(r'^editar_curso/(?P<pk>\d+)$', 'app.views.editar_curso', name='editar_curso'),
    url(r'^apagar_curso/(?P<pk>\d+)$', 'app.views.apagar_curso', name='apagar_curso'),

    url(r'^listar_coordenador', 'app.views.listar_coordenador', name='listar_coordenador'),
    url(r'^novo_coordenador', 'app.views.novo_coordenador', name='novo_coordenador'),
    url(r'^editar_coordenador/(?P<pk>\d+)$', 'app.views.editar_coordenador', name='editar_coordenador'),
    url(r'^apagar_coordenador/(?P<pk>\d+)$', 'app.views.apagar_coordenador', name='apagar_coordenador'),

    url(r'^listar_cursturma', 'app.views.listar_cursturma', name='listar_cursturma'),
    url(r'^novo_cursturma', 'app.views.novo_cursturma', name='novo_cursturma'),
    url(r'^editar_cursturma/(?P<pk>\d+)$', 'app.views.editar_cursturma', name='editar_cursturma'),
    url(r'^apagar_cursturma/(?P<pk>\d+)$', 'app.views.apagar_cursturma', name='apagar_cursturma'),

    url(r'^listar_disciplina', 'app.views.listar_disciplina', name='listar_disciplina'),
    url(r'^novo_disciplina', 'app.views.novo_disciplina', name='novo_disciplina'),
    url(r'^editar_disciplina/(?P<pk>\d+)$', 'app.views.editar_disciplina', name='editar_disciplina'),
    url(r'^apagar_disciplina/(?P<pk>\d+)$', 'app.views.apagar_disciplina', name='apagar_disciplina'),

    url(r'^listar_disciplinofertada', 'app.views.listar_disciplinofertada', name='listar_disciplinofertada'),
    url(r'^novo_disciplinofertada', 'app.views.novo_disciplinofertada', name='novo_disciplinofertada'),
    url(r'^editar_disciplinofertada/(?P<pk>\d+)$', 'app.views.editar_disciplinofertada', name='editar_disciplinofertada'),
    url(r'^apagar_disciplinofertada/(?P<pk>\d+)$', 'app.views.apagar_disciplinofertada', name='apagar_disciplinofertada'),

    url(r'^listar_grade', 'app.views.listar_grade', name='listar_grade'),
    url(r'^novo_grade', 'app.views.novo_grade', name='novo_grade'),
    url(r'^editar_grade/(?P<pk>\d+)$', 'app.views.editar_disciplina', name='editar_grade'),
    url(r'^apagar_grade/(?P<pk>\d+)$', 'app.views.apagar_grade', name='apagar_grade'),

    url(r'^listar_matricula', 'app.views.listar_matricula', name='listar_matricula'),
    url(r'^novo_matricula', 'app.views.novo_matricula', name='novo_matricula'),
    url(r'^editar_matricula/(?P<pk>\d+)$', 'app.views.editar_matricula', name='editar_matricula'),
    url(r'^apagar_matricula/(?P<pk>\d+)$', 'app.views.apagar_matricula', name='apagar_matricula'),

    url(r'^listar_periodo', 'app.views.listar_periodo', name='listar_periodo'),
    url(r'^novo_periodo', 'app.views.novo_periodo', name='novo_periodo'),
    url(r'^editar_periodo/(?P<pk>\d+)$', 'app.views.editar_periodo', name='editar_periodo'),
    url(r'^apagar_periodo/(?P<pk>\d+)$', 'app.views.apagar_periodo', name='apagar_periodo'),

    url(r'^listar_perioddisciplina', 'app.views.listar_perioddisciplina', name='listar_perioddisciplina'),
    url(r'^novo_perioddisciplina', 'app.views.novo_perioddisciplina', name='novo_perioddisciplina'),
    url(r'^editar_perioddisciplina/(?P<pk>\d+)$', 'app.views.editar_perioddisciplina', name='editar_perioddisciplina'),
    url(r'^apagar_perioddisciplina/(?P<pk>\d+)$', 'app.views.apagar_perioddisciplina', name='apagar_perioddisciplina'),

    url(r'^listar_professor', 'app.views.listar_professor', name='listar_professor'),
    url(r'^novo_professor', 'app.views.novo_professor', name='novo_professor'),
    url(r'^editar_professor/(?P<pk>\d+)$', 'app.views.editar_professor', name='editar_professor'),
    url(r'^apagar_professor/(?P<pk>\d+)$', 'app.views.apagar_professor', name='apagar_professor'),

    url(r'^listar_turma', 'app.views.listar_turma', name='listar_turma'),
    url(r'^novo_turma', 'app.views.novo_turma', name='novo_turma'),
    url(r'^editar_turma/(?P<pk>\d+)$', 'app.views.editar_turma', name='editar_turma'),
    url(r'^apagar_turma/(?P<pk>\d+)$', 'app.views.apagar_turma', name='apagar_turma'),

    url(r'^listar_questao', 'app.views.listar_questao', name='listar_questao'),
    url(r'^novo_questao', 'app.views.novo_questao', name='novo_questao'),
    url(r'^editar_questao/(?P<pk>\d+)$', 'app.views.editar_questao', name='editar_questao'),
    url(r'^apagar_questao/(?P<pk>\d+)$', 'app.views.apagar_questao', name='apagar_questao'),

    url(r'^listar_resposta', 'app.views.listar_resposta', name='listar_resposta'),
    url(r'^novo_resposta', 'app.views.novo_resposta', name='novo_resposta'),
    url(r'^editar_resposta/(?P<pk>\d+)$', 'app.views.editar_resposta', name='editar_resposta'),
    url(r'^apagar_resposta/(?P<pk>\d+)$', 'app.views.apagar_resposta', name='apagar_resposta'),

    url(r'^listar_arquivresposta', 'app.views.listar_arquivresposta', name='listar_arquivresposta'),
    url(r'^novo_arquivresposta', 'app.views.novo_arquivresposta', name='novo_arquivresposta'),
    url(r'^editar_arquivresposta/(?P<pk>\d+)$', 'app.views.editar_arquivresposta', name='editar_arquivresposta'),
    url(r'^apagar_arquivresposta/(?P<pk>\d+)$', 'app.views.apagar_arquivresposta', name='apagar_arquivresposta'),

    url(r'^listar_arquivquestao', 'app.views.listar_arquivquestao', name='listar_arquivquestao'),
    url(r'^novo_arquivquestao', 'app.views.novo_arquivquestao', name='novo_arquivquestao'),
    url(r'^editar_arquivquestao/(?P<pk>\d+)$', 'app.views.editar_arquivquestao', name='editar_arquivquestao'),
    url(r'^apagar_arquivquestao/(?P<pk>\d+)$', 'app.views.apagar_arquivquestao', name='apagar_arquivquestao'),

)
