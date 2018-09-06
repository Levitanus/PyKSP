from k_built_ins import InitCallback as _InitCallback
from k_built_ins import AsyncCompleteCallback as _AsyncCompleteCallback
from k_built_ins import ListenerCallback as _ListenerCallback
from k_built_ins import PersistenceCallback as _PersistenceCallback
from k_built_ins import PgsCallback as _PgsCallback
from k_built_ins import PolyAtCallback as _PolyAtCallback
from k_built_ins import NoteCallback as _NoteCallback
from k_built_ins import ReleaseCallback as _ReleaseCallback
from k_built_ins import MidiCallback as _MidiCallback
from k_built_ins import ControllerCallback as _ControllerCallback
from k_built_ins import RpnCallback as _RpnCallback
from k_built_ins import NrpnCallback as _NrpnCallback
from k_built_ins import UiUpdateCallback as _UiUpdateCallback


def init(f):
    '''initialization callback, executed when the script was successfully
    analyzed
    Remarks
    The init callback will be executed when:
    • clicking the "Apply" button in the script editor
    • loading a script preset or an instrument
    • restarting KONTAKT's audio engine by clicking the restart
    button in the Monitor/Engine tab or the restart button in
    KONTAKT's header
    • loading a snapshot with set_snapshot_type() set to 0'''
    _InitCallback.add_function(f)
    return f


def async_comlete(f):
    '''async complete callback, triggered after the execution of any
    load/save command
    Remarks
    To resolve synchronization issues, the commands mentioned
    above return unique IDs when being used. Upon completion of
    the command’s action, the on async_complete callback gets triggered
    and the built-in variable $NI_ASYNC_ID is updated with the ID of
    the command that triggered the callback. If the command was
    completed successfully (for example if the file was found and
    successfully loaded), the internal value $NI_ASYNC_EXIT_STATUS
    is set to 1, otherwise it is 0.'''
    _AsyncCompleteCallback.add_function(f)
    return f


def listener(f):
    '''listener callback, executed at definable time intervals or whenever
    a transport command is received
    Remarks
    The listener callback is executed at time intervals defined with the
    set_listener() command. It can also react to the host's transport
    start and stop command. This makes it the ideal callback for anything
    tempo synced like sequencers, arpeggiators, midi file player etc.
    • In some situations (like tempo changes within the host) ticks can
    be left out.'''
    _ListenerCallback.add_function(f)
    return f


def persistence_changed(f):
    '''executed after the init callback or whenever a snapshot has
    been loaded
    Remarks
    The on persistence_changed callback is called whenever the
    persistent variables change in an instrument, i.e. it is always
    executed after the init callback has been called and/or upon
    loading a snapshot.'''
    _PersistenceCallback.add_function(f)
    return f


def pgs_changed(f):
    '''executed whenever any pgs_set_key_val() command is executed in
    any script
    Remarks
    PGS stands for Program Global Storage and is a means of communication
    between script slots. See the chapter on PGS for more details.'''
    _PgsCallback.add_function(f)
    return f


def poly_at(f):
    '''polyphonic aftertouch callback, executed whenever a
    polyphonic aftertouch message is received'''
    _PolyAtCallback.add_function(f)
    return f


def note(f):
    '''note callback, executed whenever a note on message is received'''
    _NoteCallback.add_function(f)
    return f


def release(f):
    '''release callback, executed whenever a note off message is received'''
    _ReleaseCallback.add_function(f)
    return f


def controller(f):
    '''MIDI controller callback, executed whenever a CC, pitch bend
    or channel pressure message is received'''
    _ControllerCallback.add_function(f)
    return f


def rpn(f):
    '''rpn and nrpn callbacks, executed whenever a rpn or nrpn
    (registered/nonregistered parameter number) message is received'''
    _RpnCallback.add_function(f)
    return f


def nrpn(f):
    '''rpn and nrpn callbacks, executed whenever a rpn or nrpn
    (registered/nonregistered parameter number) message is received'''
    _NrpnCallback.add_function(f)
    return f


def ui_update(f):
    '''UI update callback, executed with every GUI change in KONTAKT
    Remarks
    This command is triggered with every GUI change in KONTAKT,
    so use it with caution.'''
    _UiUpdateCallback.add_function(f)
    return f


def midi_in(f):
    '''The multi script utilizes the same KSP syntax as the instrument
    scripts. Here are the main differences:
    • the multi script works on a pure MIDI event basis, i.e. you're working
    with raw MIDI data
    • there are no on note, on release and on controller callbacks
    • every MIDI event triggers the on midi_in callback
    • there are various built-in variables for the respective MIDI bytes
    The new multi script tab is accessed by clicking on the "KSP" button
    in the multi header.
    Just like instrument scripts are saved with the instrument, multi
    scripts are saved with the multi. GUI-wise everything's identical
    with the instrument script except for the height, it's limited to
    3 grid spaces (just like the instrument scripts in KONTAKT 2/3).
    The scripts are stored in a folder called "multiscripts", which
    resides next to the already existing "scripts" folder, that is,
    inside the "presets" folder:
    /Native Instruments/Kontakt 4/presets/multiscripts
    The multi script has only two callback types, the on midi_in callback
    and the various on ui_control callbacks. Each MIDI event like Note,
    Controller, Program Change etc. is triggering the on midi_in callback.
    It is very important to understand the different internal structure of
    the event processing in the multi script opposed to the instrument
    script.
    On the instrument level, you can retrieve the event IDs of notes only,
    that is, $EVENT_ID only works in the on note and on release callback.
    On the multi level, any incoming MIDI event has a unique ID which can
    be retrieved with $EVENT_ID. This means, $EVENT_ID can be a note event,
    a controller message, a program change command etc.
    This brings us to the usage of change_note(), change_velo()
    etc.commands.
    Since $EVENT_ID does not necessarily refer to a note event, this
    commands will not work in the multi script (there will be a command
    coming soon which enables you to change the MIDI bytes of events
    without having to ignore them first).
    And most important of all, remember that the multi script is really
    nothing more than a MIDI processor (whereas the instrument script is
    an event processor). A note event in the instrument script is bound
    to a voice, whereas MIDI events from the multi script are "translated'
    into note events on the instrument level. This simply means that
    play_note(), change_tune() etc. don't work in the multi script.
    You should be familiar with the basic structure of MIDI messages
    when working with the multi script.'''
    _MidiCallback.add_function(f)
    return f
