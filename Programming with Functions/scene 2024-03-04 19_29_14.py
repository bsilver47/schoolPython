from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, scene_width, scene_height)

    draw_ground(canvas, scene_width, scene_height)

    ##draw_house(canvas, house_left, house_bottom)
    ##draw_bird(canvas, bird_center, bird_top)
    ##draw_pebble(canvas, pebble_left, pebble_top, pebble_radius)
    


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 4, width = 0, fill = "tan4")

    tree_center_x = 300
    tree_bottom = 50
    tree_height = 210
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 140
    tree_bottom = 80
    tree_height = 210
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 670
    tree_bottom = 50
    tree_height = 210
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 740
    tree_bottom = 80
    tree_height = 210
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    cabin_center_x = 500
    cabin_bottom = 50
    cabin_height = 210
    draw_cabin(canvas, cabin_center_x, cabin_bottom, cabin_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline = "gray20", width = 1, fill = "tan3")

    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline = "gray20", width = 1, fill = "dark green")

def draw_cabin(canvas, center_x, bottom, height):
    panel_width = height
    panel_height = height / 8
    panel_left = center_x - panel_width / 2
    panel_right = center_x + panel_width / 2
    panel_top = bottom + panel_height

    draw_panel(canvas, bottom, panel_left, panel_right, panel_top)
    draw_panel(canvas, bottom + height / 4, panel_left, panel_right, panel_top)
    draw_panel(canvas, bottom + height / 2, panel_left, panel_right - 140, panel_top)
    draw_panel(canvas, bottom + height / 2, panel_left + 140, panel_right, panel_top)
    ##draw_panel(canvas, height, panel_left, panel_right, panel_top)

    
    roof_width = height + 2
    roof_left = center_x - roof_width / 2
    roof_right = center_x + roof_width / 2
    roof_top = bottom + height

    draw_polygon(canvas, center_x, roof_top, roof_right, height * 3 / 4, roof_left, height * 3 / 4, outline = "gray20", width = 1, fill = "firebrick")



def draw_panel(canvas, bottom, panel_left, panel_right, panel_top):
    draw_rectangle(canvas, panel_left, panel_top, panel_right, bottom, outline = "gray20", width = 1, fill = "tan3")

def draw_moon(canvas):
    draw_oval(canvas, 100, 100, 500, 500, fill = "gold1")

def draw_cloud(canvas, cloud_bottom, cloud_top, cloud_right, cloud_left):
    draw_oval(canvas, cloud_bottom, cloud_top, cloud_right, cloud_left, outline = "gray79", fill = "gray79")

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 4, scene_width, scene_height, width = 0, fill = "gray21")
    draw_moon(canvas)

    cloud_left = 425
    cloud_top = 670
    cloud_right = 800
    cloud_bottom = 450
    draw_cloud(canvas, cloud_bottom, cloud_top, cloud_right, cloud_left)

    cloud_left = 425
    cloud_top = 700
    cloud_right = 900
    cloud_bottom = 450
    draw_cloud(canvas, cloud_bottom, cloud_top, cloud_right, cloud_left)

    cloud_left = 50
    cloud_top = 250
    cloud_right = 350
    cloud_bottom = 50
    draw_cloud(canvas, cloud_bottom, cloud_top, cloud_right, cloud_left)

    half_height = round(scene_height / 2)
    min_diam = 30
    max_diam = 300

    for i in range(5):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_cloud(canvas, x, y, x + diameter, y + diameter)


# Call the main function so that
# this program will start executing.
main()