from psychopy import event, core, gui, visual
from utils import load_json, export_results

config = load_json('json_files/config.json')
trials = load_json('json_files/trials.json')

def get_participant_info():
    participant_information = {
        "Name": ""
    }
    participant_info_dialog = gui.DlgFromDict(title='PCBS Project - Stroop effect', dictionary=participant_information)
    
    if participant_info_dialog.OK:
        return participant_information
    else: 
        core.quit()

def create_window(color="white", fullscreen=True):
    window = visual.Window(color=color, fullscr=fullscreen)
    event.Mouse(visible=False)
    return window

def write_on_screen(text_category, wait_key_pressed=True, string_to_insert=None):
    text = config[text_category]
    if string_to_insert != None:
        text = text.format(string_to_insert)
    text_to_write = visual.TextStim(window, 
                        text=text,
                        anchorHoriz='center', 
                        color="Black",
                        height=0.06,
                        anchorVert='center')
    text_to_write.draw()
    window.flip()
    if wait_key_pressed:
        event.waitKeys(keyList=["space"])
    event.clearEvents()

def generate_stimuli(trial):
    left_stimulus = visual.TextStim(window, text=trial["left_stimulus_word"], color="Black")
    left_stimulus.pos = config["position"]["left"]

    center_stimulus = visual.TextStim(window, text=trial["center_stimulus_word"], color=trial["center_stimulus_color"])
    center_stimulus.pos = config["position"]["center"]

    right_stimulus = visual.TextStim(window, text=trial["right_stimulus_word"], color="Black")
    right_stimulus.pos = config["position"]["right"]

    return left_stimulus, center_stimulus, right_stimulus

def start_practise_trials():
    trial = trials[0]
    correct = False
    window.flip(clearBuffer=True)
    while(not correct):
        core.wait(.5)

        left_stimulus, right_stimulus, center_stimulus = generate_stimuli(trial)

        left_stimulus.draw()
        center_stimulus.draw()
        right_stimulus.draw()

        window.flip()

        keys = event.waitKeys(keyList=["d", "k"])
        key_pressed = keys[0]

        correct_key = "d" if trial["center_stimulus_color"] == trial["left_stimulus_word"] else "k"
        event.clearEvents()

        if key_pressed == correct_key:
            correct = True
        else:
            write_on_screen("wrong_key", wait_key_pressed=False)
            core.wait(2)

def start_experiment(participant_info):
    trial_results = []
    window.flip(clearBuffer=True)
    for trial in trials:
        core.wait(1)

        left_stimulus, right_stimulus, center_stimulus = generate_stimuli(trial)

        left_stimulus.draw()
        center_stimulus.draw()
        right_stimulus.draw()

        window.flip()
        timer = core.Clock()

        keys = event.waitKeys(keyList=["d", "k"])
        response_time = timer.getTime()
        key_pressed = keys[0]

        correct_key = "d" if trial["center_stimulus_color"] == trial["left_stimulus_word"] else "k"

        trail_result = {
            "correct": int(key_pressed == correct_key), 
            "response_time": response_time, 
            "congruent": int(trial["center_stimulus_color"] == trial["center_stimulus_word"])
        }
        trial_results.append(trail_result)
        
        event.clearEvents()
        window.flip(clearBuffer=True)
    return trial_results

if __name__ == "__main__":
    participant_info = get_participant_info()
    window = create_window()
    write_on_screen("introduction")
    write_on_screen("start_practice")
    start_practise_trials()
    write_on_screen("start_experiment")
    trail_results = start_experiment(participant_info)
    path_to_results = export_results(trail_results, participant_info, config["dir_to_store_results"])
    write_on_screen("experiment_done", string_to_insert=path_to_results)
