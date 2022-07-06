from IPython.display import Audio


def beep():
    """
    beeps at run. Useful tool in jupyter notebook.
    """
    sound_file = ''
    return Audio(sound_file, autoplay=True) 