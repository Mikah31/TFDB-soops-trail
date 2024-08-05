# TFDB soop's smart trail
This is a recreation of soop's smart trail and coupled with a generator, as the trail is ping dependent. \
The trail will seem off at times, especially when the rocket is slow or at higher pings. \
It is sadly not possible to compensate for the velocity of the rocket so a happy medium has to be found for every speed.
### Example image
![example](https://github.com/Mikah31/TFDB-soops-trail/blob/main/example.png?raw=true)

## Installation
Generate a VPK file using the python script **vpk_generator.py** and copy the generated VPK into: **Team Fortress 2\tf\custom**

## Notes
- Modifications can be made to **custom_vpk\particles\rockettrail.pcf** and the generator should still work if the attribute: **`Remap Distance Between Two Control Points to Scalar`** remains (largely) untouched.
- Sounds should also be able to be bundled into the VPK, although this is untested.
- The trail is not perfect (except at 0 ping), so expect it to be more of a guideline.
- The circle is way bigger at lower fov's, especially in first person, so be aware of that.

## Credits
1. The original trail created by soop | [Link](https://www.youtube.com/watch?v=C5735HWVj9s)
2. This variation of the snowball mod is modified from Choden's snowball mod | [Link](https://github.com/flawfree/tfdbqol)
