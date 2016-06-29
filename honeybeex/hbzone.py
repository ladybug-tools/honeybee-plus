from honeybee.hbzone import HBZone as Zone
import config


class HBZone(Zone):
    """Honeybee Zone.

    Args:
        name: Unique name for this zone.
        origin: Zone origin point (default: 0, 0, 0)
        geometryRules: EnergyPlus geometryRules. (default: "LowerLeftCorner";
            "CounterClockWise"; "Absolute")
        buildingProgram: HBZone building program.
        zoneProgram: Specific program for this zone from the available building
            programs.
        isConditioned: A boolean that indicates if the zone is conditioned.
            (default: True)
    """

    @property
    def geometry(self):
        """Return zone geometry for visualization."""
        _geo = []
        for surface in self.surfaces:
            _geo.append(surface.geometry)
            if surface.hasChildSurfaces:
                for childSurface in surface.childrenSurfaces:
                    _geo.append(childSurface.geometry)

        return _geo
