from psychopy import event, core, data, gui, visual
import json

config_file = open('config.json', "r")
config = json.load(config_file)
config_file.close()

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
    window = visual.Window(monitor="testMonitor", color=color, fullscr=fullscreen)
    event.Mouse(visible=False)
    return window

def introduce_experiment():
    introduction = visual.TextStim(window, 
                        text=config["introduction"],
                        alignHoriz='center', 
                        color="Black",
                        alignVert='center')
    introduction.draw()
    window.flip()
    event.waitKeys()
    event.clearEvents()


if __name__ == "__main__":
    participant_info = get_participant_info()
    window = create_window()
    introduce_experiment()



