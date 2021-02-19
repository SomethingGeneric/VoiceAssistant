from gtts import gTTS
from io import BytesIO
import pyglet

pyglet.options["audio"] = ("pulse",)


def log(t):
    # Add file later
    print(t)


def info(t):
    log("[I] - " + t)


def err(t, fail=False):
    log("[E] - " + t)
    if fail:
        sys.exit(1)


def speak(words: str, lang: str = "en"):
    info("Reply: " + words)
    try:
        info("Speaking: " + words)
        with BytesIO() as f:
            gTTS(text=words, lang=lang).write_to_fp(f)
            f.seek(0)

            player = pyglet.media.load("_.mp3", file=f).play()
            while player.playing:
                pyglet.app.platform_event_loop.dispatch_posted_events()
                pyglet.clock.tick()
        info("Done speaking.")
    except Exception as e:
        err("Speaking failed: " + str(e))


def sanitize(blacklist, string):
    for item in blacklist:
        string = string.replace(item, "")
    return string
