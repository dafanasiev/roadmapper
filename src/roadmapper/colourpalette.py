# MIT License

# Copyright (c) 2022 CS Goh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from dataclasses import dataclass, field

### Font :
# "Microsoft YaHei UI"
# "DengXian"
# "Segoe UI"
# "Tahoma"
# "Microsoft Jhenghei"
# simhei.ttf
# "ARIALUNI.TTF"

DEFAULT_FONT = "arial.ttf"
DEFAULT_TITLE_FONT_SIZE = 26
DEFAULT_SUBTITLE_FONT_SIZE = 18
DEFAULT_TIMELINE_FONT_SIZE = 12
DEFAULT_MARKER_FONT_SIZE = 12
DEFAULT_GROUP_FONT_SIZE = 12
DEFAULT_TASK_FONT_SIZE = 12
DEFAULT_MILESTONE_FONT_SIZE = 10
DEFAULT_FOOTER_FONT_SIZE = 13


default_colour_settings = {
    "theme": "DEFAULT",
    "settings": {
        "background": {
            "background_fill_colour": "#FFFFFF",
        },
        "title": {
            "title_font": DEFAULT_FONT,
            "title_font_size": DEFAULT_TITLE_FONT_SIZE,
            "title_font_colour": "#000000",
            "subtitle_font": DEFAULT_FONT,
            "subtitle_font_size": DEFAULT_SUBTITLE_FONT_SIZE,
            "subtitle_font_colour": "#000000",
        },
        "timeline": {
            "timeline_font": DEFAULT_FONT,
            "timeline_font_size": DEFAULT_TIMELINE_FONT_SIZE,
            "timeline_font_colour": "#FFFFFF",
            "timeline_fill_colour": "#000000",
        },
        "marker": {
            "marker_font": DEFAULT_FONT,
            "marker_font_size": DEFAULT_MARKER_FONT_SIZE,
            "marker_font_colour": "#000000",
            "marker_line_colour": "#000000",
        },
        "group": {
            "group_font": DEFAULT_FONT,
            "group_font_size": DEFAULT_GROUP_FONT_SIZE,
            "group_font_colour": "#FFFFFF",
            "group_fill_colour": "#000000",
        },
        "task": {
            "task_font": DEFAULT_FONT,
            "task_font_size": DEFAULT_TASK_FONT_SIZE,
            "task_font_colour": "#000000",
            "task_fill_colour": "#D9D9D9",
        },
        "milestone": {
            "milestone_font": DEFAULT_FONT,
            "milestone_font_size": DEFAULT_MILESTONE_FONT_SIZE,
            "milestone_font_colour": "#000000",
            "milestone_fill_colour": "#000000",
        },
        "footer": {
            "footer_font": DEFAULT_FONT,
            "footer_font_size": DEFAULT_FOOTER_FONT_SIZE,
            "footer_font_colour": "#000000",
        },
    },
}

greywoof_colour_settings = {
    "theme": "GREYWOOF",
    "settings": {
        "background": {
            "background_fill_colour": "#FFFFFF",
        },
        "title": {
            "title_font": DEFAULT_FONT,
            "title_font_size": DEFAULT_TITLE_FONT_SIZE,
            "title_font_colour": "#000000",
            "subtitle_font": DEFAULT_FONT,
            "subtitle_font_size": DEFAULT_SUBTITLE_FONT_SIZE,
            "subtitle_font_colour": "#000000",
        },
        "timeline": {
            "timeline_font": DEFAULT_FONT,
            "timeline_font_size": DEFAULT_TIMELINE_FONT_SIZE,
            "timeline_font_colour": "#FFFFFF",
            "timeline_fill_colour": "#666666",
        },
        "marker": {
            "marker_font": DEFAULT_FONT,
            "marker_font_size": DEFAULT_MARKER_FONT_SIZE,
            "marker_font_colour": "#000000",
            "marker_line_colour": "#000000",
        },
        "group": {
            "group_font": DEFAULT_FONT,
            "group_font_size": DEFAULT_GROUP_FONT_SIZE,
            "group_font_colour": "#FFFFFF",
            "group_fill_colour": "#666666",
        },
        "task": {
            "task_font": DEFAULT_FONT,
            "task_font_size": DEFAULT_TASK_FONT_SIZE,
            "task_font_colour": "#000000",
            "task_fill_colour": "#D9D9D9",
        },
        "milestone": {
            "milestone_font": DEFAULT_FONT,
            "milestone_font_size": DEFAULT_MILESTONE_FONT_SIZE,
            "milestone_font_colour": "#000000",
            "milestone_fill_colour": "#B7B7B7",
        },
        "footer": {
            "footer_font": DEFAULT_FONT,
            "footer_font_size": DEFAULT_FOOTER_FONT_SIZE,
            "footer_font_colour": "#000000",
        },
    },
}

bluemountain_colour_settings = {
    "theme": "BLUEMOUNTAIN",
    "settings": {
        "background": {
            "background_fill_colour": "#FFFFFF",
        },
        "title": {
            "title_font": DEFAULT_FONT,
            "title_font_size": DEFAULT_TITLE_FONT_SIZE,
            "title_font_colour": "#0B5394",
            "subtitle_font": DEFAULT_FONT,
            "subtitle_font_size": DEFAULT_SUBTITLE_FONT_SIZE,
            "subtitle_font_colour": "#0B5394",
        },
        "timeline": {
            "timeline_font": DEFAULT_FONT,
            "timeline_font_size": DEFAULT_TIMELINE_FONT_SIZE,
            "timeline_font_colour": "#FFFFFF",
            "timeline_fill_colour": "#0B5394",
        },
        "marker": {
            "marker_font": DEFAULT_FONT,
            "marker_font_size": DEFAULT_MARKER_FONT_SIZE,
            "marker_font_colour": "#0B5394",
            "marker_line_colour": "#0B5394",
        },
        "group": {
            "group_font": DEFAULT_FONT,
            "group_font_size": DEFAULT_GROUP_FONT_SIZE,
            "group_font_colour": "#FFFFFF",
            "group_fill_colour": "#0B5394",
        },
        "task": {
            "task_font": DEFAULT_FONT,
            "task_font_size": DEFAULT_TASK_FONT_SIZE,
            "task_font_colour": "#000000",
            "task_fill_colour": "#9FC5E8",
        },
        "milestone": {
            "milestone_font": DEFAULT_FONT,
            "milestone_font_size": DEFAULT_MILESTONE_FONT_SIZE,
            "milestone_font_colour": "#0B5394",
            "milestone_fill_colour": "#3D85C6",
        },
        "footer": {
            "footer_font": DEFAULT_FONT,
            "footer_font_size": DEFAULT_FOOTER_FONT_SIZE,
            "footer_font_colour": "#0B5394",
        },
    },
}

orangepeel_colour_settings = {
    "theme": "ORANGEPEEL",
    "settings": {
        "background": {
            "background_fill_colour": "#FFFFFF",
        },
        "title": {
            "title_font": DEFAULT_FONT,
            "title_font_size": DEFAULT_TITLE_FONT_SIZE,
            "title_font_colour": "#B45F06",
            "subtitle_font": DEFAULT_FONT,
            "subtitle_font_size": DEFAULT_SUBTITLE_FONT_SIZE,
            "subtitle_font_colour": "#B45F06",
        },
        "timeline": {
            "timeline_font": DEFAULT_FONT,
            "timeline_font_size": DEFAULT_TIMELINE_FONT_SIZE,
            "timeline_font_colour": "#FFFFFF",
            "timeline_fill_colour": "#B45F06",
        },
        "marker": {
            "marker_font": DEFAULT_FONT,
            "marker_font_size": DEFAULT_MARKER_FONT_SIZE,
            "marker_font_colour": "#B45F06",
            "marker_line_colour": "#B45F06",
        },
        "group": {
            "group_font": DEFAULT_FONT,
            "group_font_size": DEFAULT_GROUP_FONT_SIZE,
            "group_font_colour": "#FFFFFF",
            "group_fill_colour": "#B45F06",
        },
        "task": {
            "task_font": DEFAULT_FONT,
            "task_font_size": DEFAULT_TASK_FONT_SIZE,
            "task_font_colour": "#000000",
            "task_fill_colour": "#F6B26B",
        },
        "milestone": {
            "milestone_font": DEFAULT_FONT,
            "milestone_font_size": DEFAULT_MILESTONE_FONT_SIZE,
            "milestone_font_colour": "#B45F06",
            "milestone_fill_colour": "#B45F06",
        },
        "footer": {
            "footer_font": DEFAULT_FONT,
            "footer_font_size": DEFAULT_FOOTER_FONT_SIZE,
            "footer_font_colour": "#B45F06",
        },
    },
}

greenturtle_colour_settings = {
    "theme": "GREENTURTLE",
    "settings": {
        "background": {
            "background_fill_colour": "#FFFFFF",
        },
        "title": {
            "title_font": DEFAULT_FONT,
            "title_font_size": DEFAULT_TITLE_FONT_SIZE,
            "title_font_colour": "#38761D",
            "subtitle_font": DEFAULT_FONT,
            "subtitle_font_size": DEFAULT_SUBTITLE_FONT_SIZE,
            "subtitle_font_colour": "#38761D",
        },
        "timeline": {
            "timeline_font": DEFAULT_FONT,
            "timeline_font_size": DEFAULT_TIMELINE_FONT_SIZE,
            "timeline_font_colour": "#FFFFFF",
            "timeline_fill_colour": "#38761D",
        },
        "marker": {
            "marker_font": DEFAULT_FONT,
            "marker_font_size": DEFAULT_MARKER_FONT_SIZE,
            "marker_font_colour": "#38761D",
            "marker_line_colour": "#38761D",
        },
        "group": {
            "group_font": DEFAULT_FONT,
            "group_font_size": DEFAULT_GROUP_FONT_SIZE,
            "group_font_colour": "#FFFFFF",
            "group_fill_colour": "#38761D",
        },
        "task": {
            "task_font": DEFAULT_FONT,
            "task_font_size": DEFAULT_TASK_FONT_SIZE,
            "task_font_colour": "#000000",
            "task_fill_colour": "#93C47D",
        },
        "milestone": {
            "milestone_font": DEFAULT_FONT,
            "milestone_font_size": DEFAULT_MILESTONE_FONT_SIZE,
            "milestone_font_colour": "#38761D",
            "milestone_fill_colour": "#38761D",
        },
        "footer": {
            "footer_font": DEFAULT_FONT,
            "footer_font_size": DEFAULT_FOOTER_FONT_SIZE,
            "footer_font_colour": "#38761D",
        },
    },
}

ColourThemesSettings = [
    default_colour_settings,
    greywoof_colour_settings,
    bluemountain_colour_settings,
    orangepeel_colour_settings,
    greenturtle_colour_settings,
    ### Add more themes here
]

@dataclass
class ColourTheme:
    """Colour theme for the Roadmapper."""

    def __init__(self, colour_theme_name: str) -> None:
        """Initialise the colour theme."""

        found = False
        for theme in ColourThemesSettings:
            if theme["theme"] == colour_theme_name:
                found = True

        if found == False:
            raise ValueError(f"Colour theme {colour_theme_name} not recognised.")

        self._colour_theme_name = colour_theme_name

    def get_colour_theme_settings(self, roadmap_component: str) -> tuple:
        """Get the colour theme settings for the specified roadmap component.

        Args:
            roadmap_component (str): Roadmap component to get the colour theme settings for.
                                        Components are: "background", "title", "timeline", "marker", "group", "task", "milestone", "footer"

        Returns:
            background_colour (str): If roadmap_component is "background"

        title_font_colour (str): If roadmap_component is "title"
        subtitle_font_colour (str): If roadmap_component is "title"

        timeline_font_colour (str): If roadmap_component is "timeline"
        timeline_fill_colour (str): If roadmap_component is "timeline"

        marker_font_colour (str): If roadmap_component is "marker"
        marker_line_colour (str): If roadmap_component is "marker"

        group_font_colour (str): If roadmap_component is "group"
        group_fill_colour (str): If roadmap_component is "group"

        task_font_colour (str): If roadmap_component is "task"
        task_fill_colour (str): If roadmap_component is "task"

        milestone_font_colour (str): If roadmap_component is "milestone"
        milestone_fill_colour (str): If roadmap_component is "milestone"

        footer_font_colour (str): If roadmap_component is "footer"
        """

        colour_settings = None

        for _, value in enumerate(ColourThemesSettings):
            if value["theme"] == self._colour_theme_name:
                colour_settings = value["settings"]
                break

        ### get the colour scheme for the specified roadmap component
        return tuple(colour_settings[roadmap_component].values())
