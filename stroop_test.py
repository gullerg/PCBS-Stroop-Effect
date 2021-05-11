from psychopy import event, core, data, gui, visual
import json

from utils import *


config = load_json('json_files/config.json')
trials = load_json('json_files/trials.json')

def get_participant_info():
    participant_information = {
        "Age": "",
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

def write_on_screen(text):
    introduction = visual.TextStim(window, 
                        text=config[text],
                        anchorHoriz='center', 
                        color="Black",
                        anchorVert='center')
    introduction.draw()
    window.flip()
    event.waitKeys()
    event.clearEvents()

def generate_stimuli(trial):
    left_stimulus = visual.TextStim(window, text=trial["left_stimulus"], color="Black")
    left_stimulus.pos = config["position"]["left"]

    center_stimulus = visual.TextStim(window, text=trial["center_stimulus"], color=trial["center_stimulus_color"])
    center_stimulus.pos = config["position"]["center"]

    right_stimulus = visual.TextStim(window, text=trial["right_stimulus"], color="Black")
    right_stimulus.pos = config["position"]["right"]

    return left_stimulus, center_stimulus, right_stimulus

def start_practise_trials():
    trial = trials[0]
    correct = False
    while(not correct):
        core.wait(.5)

        left_stimulus, right_stimulus, center_stimulus = generate_stimuli(trial)

        left_stimulus.draw()
        center_stimulus.draw()
        right_stimulus.draw()

        window.flip()

        keys = event.waitKeys(keyList=["d", "k"])
        key_pressed = keys[0]

        correct_key = "d" if trial["center_stimulus_color"] == trial["left_stimulus"] else "k"
        event.clearEvents()

        if key_pressed == correct_key:
            correct = True

def start_experiment(participant_info):
    results = []
    timer = core.Clock()
    for trial in trials:
        core.wait(.5)

        left_stimulus, right_stimulus, center_stimulus = generate_stimuli(trial)

        left_stimulus.draw()
        center_stimulus.draw()
        right_stimulus.draw()

        window.flip()
        timer.reset()

        keys = event.waitKeys(keyList=["d", "k"])
        resp_time = timer.getTime()

        key_pressed = keys[0]

        correct_key = "d" if trial["center_stimulus_color"] == trial["left_stimulus"] else "k"

        result = {
            "correct": int(key_pressed == correct_key), 
            "response_time": resp_time, 
            "match": int(trial["center_stimulus_color"] == trial["center_stimulus"])
        }

        results.append(result)
        event.clearEvents()
    return results



if __name__ == "__main__":
    participant_info = get_participant_info()
    window = create_window()
    write_on_screen("introduction")
    write_on_screen("start_practice")
    start_practise_trials()
    write_on_screen("start_experiment")
    results = start_experiment(participant_info)
    export_results(results, participant_info, config["dir_to_store_results"])
    write_on_screen("experiment_done")


