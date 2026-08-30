import time
import pytest

from src.adapters.tkinter.gui_main import create_app


# TC1 – Typical name: "Jermaine" → "Hello Jermaine!"
@pytest.mark.gui
def test_gui_tc1_typical_name():
    root, name_entry, greet_button, output_label = create_app()
    try:
        name_entry.insert(0, "Jermaine")
        greet_button.invoke()
        root.update_idletasks()

        assert output_label.cget("text") == "Hello Jermaine!"
    finally:
        root.destroy()


# TC2 – Alternate name: "Maria" → "Hello Maria!"
@pytest.mark.gui
def test_gui_tc2_alternate_name():
    root, name_entry, greet_button, output_label = create_app()
    try:
        name_entry.insert(0, "Maria")
        greet_button.invoke()
        root.update_idletasks()

        assert output_label.cget("text") == "Hello Maria!"
    finally:
        root.destroy()


# TC3 – Blank input: [Enter] → "Hello there!"
@pytest.mark.gui
def test_gui_tc3_blank_input():
    root, name_entry, greet_button, output_label = create_app()
    try:
        # leave entry empty on purpose
        greet_button.invoke()
        root.update_idletasks()

        assert output_label.cget("text") == "Hello there!"
    finally:
        root.destroy()


# TC4 – Spaces only: "   " → "Hello there!"
@pytest.mark.gui
def test_gui_tc4_spaces_only():
    root, name_entry, greet_button, output_label = create_app()
    try:
        name_entry.insert(0, "   ")
        greet_button.invoke()
        root.update_idletasks()

        assert output_label.cget("text") == "Hello there!"
    finally:
        root.destroy()


# TC5 – Long name → "Hello Supercalifragilisticexpialidocious!"
@pytest.mark.gui
def test_gui_tc5_long_name():
    root, name_entry, greet_button, output_label = create_app()
    try:
        long_name = "Supercalifragilisticexpialidocious"
        name_entry.insert(0, long_name)
        greet_button.invoke()
        root.update_idletasks()

        expected = f"Hello {long_name}!"
        assert output_label.cget("text") == expected
    finally:
        root.destroy()


# TC6 – Performance: any input → output under 1 second
@pytest.mark.gui
@pytest.mark.performance
def test_gui_tc6_performance_under_one_second():
    root, name_entry, greet_button, output_label = create_app()
    try:
        name_entry.insert(0, "PerfTest")

        start = time.perf_counter()
        greet_button.invoke()
        root.update_idletasks()
        end = time.perf_counter()

        # sanity check: greeting is correct
        assert output_label.cget("text") == "Hello PerfTest!"
        # performance requirement: under 1 second
        assert (end - start) < 1.0
    finally:
        root.destroy()
