# Problem 2 - Corkboard

In this problem, you will create a graphics program that makes use of images and transformations.

## Basic Requirements (3C and 4C)

### Level 2

Add the `corkboard.jpg` image as the background.
* The screen should already be the right size to fit this image and no transformations are necessary.

Add at least 5 of your own images, that include:
* A picture of you with some other people.
* A postcard of a destination that you want to travel to.
* A poster of your favourite band or from your favourite movie/show.
* A picture of a pet.
* Some object that is not a rectangle and has a transparent background (e.g. award ribbon/medal, team banner/flag).

These images should be:
* Scaled to an appropriate size
* At least 2 pictures should be rotated to look like they were added haphazardly.

### Level 3

Add a copy of the `pushpin.png` image to each of the images from step 2.
* Convert the pixel format of the image.  Note that this image has a transparent background.
* Scale the push pin to an appropriate size.
* Push pins on the left side of the board need to be flipped horizontally so they point the other way.

Some notes about using the same image multiple times:
* You should only have to load the image once, but blit it multiple times.
* You do NOT need five copies of the push pin image.  Three is the maximum you need (original, scaled, flipped).

### Level 4

Find your own true type font online and upload the `.ttf` file to your repl.  Render your name into an image using that font and position it in the center of the screen.

### Sample

Here is what Mr. Devet's program looks like:

![Mr. Devet's Cork Board](https://mrdevet.github.io/ICS3C/assets/images/corkboard_screenshot.png)

## Advanced Requirements (4C only)

**_TBD_**

## Submitting

When you are finished, push your code to GitHub.  Submit it on [Gradescope](gradescope.com) where it will be graded manually for correctness (80%) and style (20% - see [Style Guide](https://mrdevet.github.io/ICS3C/assignments/Style-Guide/)).

## Resources

The following lessons will be helpful with this exercise:

* **[Images](https://mrdevet.github.io/ICS3C/graphics/drawing/3-Images/)**
  * [Image Files](https://mrdevet.github.io/ICS3C/graphics/drawing/3b-Images/)

* **[Transformations and Text](https://mrdevet.github.io/ICS3C/graphics/drawing/4-Transformations-Text/)**
  * [Transforming Images](https://mrdevet.github.io/ICS3C/graphics/drawing/4a-Transformations/)
  * [Positioning Images](https://mrdevet.github.io/ICS3C/graphics/drawing/4b-Positioning/)
  * [Text](https://mrdevet.github.io/ICS3C/graphics/drawing/4c-Text/)

Use the [Pygame Cheat Sheet](https://mrdevet.github.io/ICS3C/graphics/cheat-sheet/) to easily find information on each function/method you might need.