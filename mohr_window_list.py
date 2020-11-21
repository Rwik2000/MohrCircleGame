
import window_types.mohr_quiz as mohr_quiz
import window_types.mohr_general as mohr_general
import window_types.pop_up as pop_up
import window_types.mohr_initial as mohr_initial

from utilities.mohr_screen import *

windows = {mohr_initial.startwindow : ['startwindow',startwindow_check],
            mohr_initial.enterwindow : ["enterwindow", enterWindow_check],
            mohr_general.generalwindow : ["generalwindow",generalwindow_check],
            mohr_general.general2D_input_window : ["general2D_input_window", general2D_input_window_check],
            mohr_general.general3D_input_window :["general3D_input_window", general3D_input_window_check],
            mohr_quiz.quizwindow:["quizwindow",quizwindow_check],
            mohr_quiz.quizwindow_2d:["quizwindow_2d",quizwindow_2d_check],
            mohr_quiz.quizwindow_3d:["quizwindow_3d",quizwindow_3d_check],
            mohr_quiz.quizwindow_concept:["quizwindow_concept",quizwindow_concept_check],
            mohr_quiz.quiz_end_window:["quiz_end_window",quiz_end_window_check],
            mohr_quiz.eval_window:["eval_window",eval_window_check],
            pop_up.incompatible_input_window:["incompatible_input_window",incompatible_input_window_check]}