
import window_types.mohr_quiz as mohr_quiz
import window_types.mohr_general as mohr_general
import window_types.pop_up as pop_up
import window_types.mohr_initial as mohr_initial

from utilities.mohr_screen import *

windows = {"startwindow" : [mohr_initial.startwindow,startwindow_check],
            "enterwindow" : [mohr_initial.enterwindow, enterWindow_check],
            "generalwindow" : [ mohr_general.generalwindow,generalwindow_check],
            "gen2D_stress_input_window" : [mohr_general.gen2D_stress_input_window, gen2D_stress_input_window_check],
            "gen3D_stress_input_window" :[mohr_general.gen3D_stress_input_window, gen3D_stress_input_window_check],
            "gen2D_strain_input_window" : [mohr_general.gen2D_strain_input_window, gen2D_strain_input_window_check],
            "gen3D_strain_input_window" :[mohr_general.gen3D_strain_input_window, gen3D_strain_input_window_check],
            "stress_strain_window" :[mohr_general.stress_strain_window, stress_strain_window_check],
            "quizwindow":[mohr_quiz.quizwindow,quizwindow_check],
            "quizwindow_2d":[mohr_quiz.quizwindow_2d,quizwindow_2d_check],
            "quizwindow_3d":[mohr_quiz.quizwindow_3d,quizwindow_3d_check],
            "quizwindow_concept":[mohr_quiz.quizwindow_concept,quizwindow_concept_check],
            "quiz_end_window":[mohr_quiz.quiz_end_window,quiz_end_window_check],
            "eval_window":[mohr_quiz.eval_window,eval_window_check],
            "incompatible_input_window":[pop_up.incompatible_input_window,incompatible_input_window_check]}