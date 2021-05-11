from psychopy import event, core, data, gui, visual
import json

config_file = open('config.json', "r")
config = json.load(config_file)
config_file.close()

trials_file = open('trials.json', "r")
trials = json.load(trials_file)
trials_file.close()

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

def introduce_experiment():
    introduction = visual.TextStim(window, 
                        text=config["introduction"],
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

def start_experiment():
    results = []
    timer = core.Clock()
    for trial in trials:

        left_stimulus, right_stimulus, center_stimulus = generate_stimuli(trial)

        left_stimulus.draw()
        center_stimulus.draw()
        right_stimulus.draw()

        window.flip()

        core.wait(.6)
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

        print(result)


if __name__ == "__main__":
    participant_info = get_participant_info()
    window = create_window()
    introduce_experiment()
    start_experiment()


