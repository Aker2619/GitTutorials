# How to Download Additional Voices on macOS

The macOS `say` command uses voices installed on your system. You can download more voices through System Settings.

## Steps to Download New Voices

1. Open **System Settings**
2. Navigate to **Accessibility** → **Spoken Content**
3. Click the dropdown next to **System Voice**
4. Select **Manage Voices...**
5. Browse and download any voices you want

## Using Downloaded Voices

Once downloaded, the voices appear when you run:

```bash
say -v ?
```

Use them in Python with:

```python
import subprocess

voice = "YourNewVoice"
subprocess.run(["say", "-v", voice, "Hello world"])
```

## Popular Voice Categories

- **English (US)**: Samantha, Alex, Ava, Tom
- **English (UK)**: Daniel, Kate, Oliver
- **English (Australia)**: Karen, Lee
- **English (Ireland)**: Moira
- **Other Languages**: French, Spanish, German, Japanese, and many more

## Tips

- Premium/enhanced voices sound more natural but use more storage
- Some voices support different speaking rates with the `-r` flag (words per minute)
- Test voices quickly in Terminal: `say -v Alex "Testing this voice"`
