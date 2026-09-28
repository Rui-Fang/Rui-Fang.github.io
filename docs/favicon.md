# Fish favicon

The source is the user's `QQ截图20240325211313 - 副本.png`, compared against the 18 supplied avatar variants. `images/fish-head.png` is a native-resolution 438 × 421 crop of its head. Its opaque RGB pixels are unchanged; an alpha mask removes the background, shadow, clothing, and the joins between the head outline and clothing. The face was not redrawn or generated.

The comparison normalized image dimensions and used SIFT matches with a RANSAC similarity transform. Duplicate target matches and degenerate transforms were excluded. The matching 903-pixel versions were compared on their original coordinate grid.

Within the selected head mask:

- The March 2023 and March 2024 undecorated PNGs have identical RGB values at 99.824% of pixels.
- Across all 18 aligned versions, 98.185% of pixels agree with the reference's black/non-black classification in at least 10 versions. This is a coarse structural check, not an RGB fidelity score.
- Only 0.422% are RGB-identical in all 18 aligned images. JPEG compression, resampling, palette changes, masks, glasses, hats, and altered expressions make a literal intersection unsuitable as an image.

These comparisons support retaining an unoccluded original, including its irregular outline, angular mouth, narrow eye and highlight, and later-version forehead dots. The final image uses the reference's original colors and lines rather than averaging differently colored or occluded faces.

The requested white-face variant is `images/fish-head-white.png`; the original-color `fish-head.png` remains the source. The white variant changes the face fill to pure white while retaining the original silhouette and a transparent exterior.

Run `python3 scripts/build_favicon.py` with Pillow installed to export the white-face master, 16/32/48/64-pixel PNGs and the matching multi-resolution ICO. The script centers the native crop with approximately 4% transparent padding per side. It resamples black-ink and alpha coverage separately, strengthens subpixel strokes with size-specific contrast, and retains a narrow antialiased edge. The 16-pixel frame also shifts horizontally by a quarter pixel to better align its strokes with the pixel grid. Larger frames receive milder processing.

The 16/32-pixel frames have explicit optical corrections: a continuous four-neighbor contour, a pixel-hinted eye/white separation and a narrower descending mouth at 16 pixels, and repaired eyelid/highlight pixels at 32 pixels. These small-size corrections intentionally differ from literal downsampling; the original master is unchanged.

Each ICO frame is supplied explicitly to preserve these adjustments instead of letting the encoder rescale a single master. HTML declares the actual PNG sizes for different display densities; the favicon query version invalidates previously cached images. Pixel identity applies only to the native head master. Small sizes deliberately trade exact area-averaged colors for clearer linework.
