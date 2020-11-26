class Screen_check():
    def __init__(self):
        self.current = False

    def makeCurrent(self):
        self.current = True

    def endCurrent(self):
        self.current = False

    def checkUpdate(self):
        return self.current

startwindow_check = Screen_check()
enterWindow_check = Screen_check()
generalwindow_check = Screen_check()
gen2D_stress_input_window_check = Screen_check()
gen3D_stress_input_window_check = Screen_check()
gen2D_strain_input_window_check = Screen_check()
gen3D_strain_input_window_check = Screen_check()
stress_strain_window_check = Screen_check()
quizwindow_check = Screen_check()
quizwindow_2d_check = Screen_check()
ansQuiz_2d_check = Screen_check()
quizwindow_3d_check = Screen_check()
quizwindow_start_check = Screen_check()
quizwindow_concept_check = Screen_check()
quiz_end_window_check = Screen_check()
eval_window_check = Screen_check()
incompatible_input_window_check = Screen_check()