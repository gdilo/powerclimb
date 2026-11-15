# PowerClimb native UI tokens

Synced from Android resources, not a web stylesheet. Only existing values are recorded.

## Colors
| Token | Value | Source / usage |
| --- | --- | --- |
| Window background | `#000000` | `app/src/main/res/values/styles.xml`, Android black window/system bars |
| White | `#FFFFFF` | `app/src/main/res/values-night/colors.xml`, primary night text; drawable lightning |
| Secondary on dark | Android `#B3FFFFFF` / CSS `rgba(255,255,255,0.7)` | `app/src/main/res/values-night/colors.xml` |
| Accent | `#FFF500` | `app/src/main/res/values/colors.xml`, pc_zone3; theme colorAccent |
| Icon mountain | `#FFD400` | `app/src/main/res/drawable/ic_powerclimb.xml` |
| Back surface | `#A0B4BE` | `app/src/main/res/values/colors.xml`, pc_back_background; sampled from captured Karoo app-info reference at20,710 |

## Typography
- Application: native Android `sans`, from `app/src/main/res/values/styles.xml`; HTML preview uses `system-ui, sans-serif` as its system-font approximation.
- Data fields use Relative and IBM Plex Sans Condensed in `app/src/main/res/layout/powerclimb_field.xml`. They are not used or changed by the informational screen.
- No shared application-screen type-size tokens exist; the minimal screen has local title/body sizes rather than changing field typography.

## Spacing and icon
- `4dp` padding and `8dp` label gap exist in `app/src/main/res/layout/powerclimb_field.xml`; compose the informational screen spacing from that rhythm.
- Existing icon: `24dp` viewport, mountain and lightning paths in `app/src/main/res/drawable/ic_powerclimb.xml`.

## Radius, shadows and components
- No card/shadow tokens. Navigation-only right corners are27dp in `app/src/main/res/drawable/back_navigation_background.xml`; no new cards or shadows.
- Application uses `android:style/Theme.Material.NoActionBar`; keep native scrolling, system Back and text, with no settings or data controls.
- Data fields remain unchanged. Following the user's concrete KeyEvent example, the compact lower-left54dp framework ImageButton overlays the full-height summary, using `ic_back.xml` and `back_navigation_background.xml`. `launcher_summary.xml` reserves no bottom viewport row; only scroll-content end padding is70dp (54dpcontrol +8dpmargin +8dpgap), so final lines can move clear of the overlay. It dispatches KEYCODE_BACK ACTION_DOWN then ACTION_UP, the same framework route as physical Back. It is an app-owned Karoo-style affordance, not a firmware-provided UI component; do not claim otherwise.
