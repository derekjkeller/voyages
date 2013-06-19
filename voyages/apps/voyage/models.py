from django.db import models

class Voyage(models.Model):
    """
    Information about voyages.
    """

    class BroadRegion(models.Model):
        """
        Broad Regions (continents).
        """

        broad_region = models.CharField("Broad region", max_length=35)

    class SpecificRegion(models.Model):
        """
        Specific Regions (countries or colonies).
        related to: :model:`voyages.apps.voyages.Voyage.BroadRegion`
        """

        specific_region = models.CharField("Specific region (country or colony",
                                           max_length=35)
        broad = models.ForeignKey('BroadRegion')

    class Place(models.Model):
        """
        Place (port or location).
        related to: :model:`voyages.apps.voyages.Voyage.BroadRegion`
        related to: :model:`voyages.apps.voyages.Voyage.SpecificRegion`
        """
        place_name = models.CharField(max_length=35)
        broad_region = models.ForeignKey('BroadRegion')
        specific_region = models.ForeignKey('SpecificRegion')

    class VoyageGroupings(models.Model):
        """
        Labels for groupings names.
        """
        grouping_name = models.CharField(max_length=30)

    class VoyageShip(models.Model):
        """
        Information about voyage ship.
        related to: :model:`voyages.apps.voyages.Voyage.SpecificRegion`
        related to: :model:`voyages.apps.voyages.Voyage.Place`

        """
        class VoyageVentureOwner(models.Model):
            """
            Information about other owners.
            """
            number_of_owner = models.IntegerField(max_length=2, blank=True)
            name_of_owner = models.CharField(max_length=40)

        class NationalityOfShip(models.Model):
            """
            Nationalities of ships.
            """
            nationality_of_ship = models.CharField(max_length=35)

        class ImputedCountryShip(models.Model):
            """
            Imputed country in which ship registered.
            """
            imputed_country = models.CharField("Imputed country "
                                               "in which ship registered.",
                                               max_length=35)

        class TonType(models.Model):
            """
            Types of tonnage.
            """
            ton_type = models.CharField(max_length=35)

        class RigOfVessel(models.Model):
            """
            Rig of Vessel.
            """
            rig_of_vessel = models.CharField(max_length=25)

        # Data variables
        ship_name = models.CharField("Name of vessel", max_length=60)
        nationality = models.ForeignKey('NationalityOfShip')
        tonnage = models.IntegerField("Tonnage of vessel", max_length=4,
                                       blank=True)
        ton_type = models.ForeignKey('TonType')
        rig_of_vessel = models.ForeignKey('RigOfVessel')
        guns_mounted = models.IntegerField("Guns mounted", max_length=2,
                                            blank=True)
        year_of_construction = models.DateField\
                ("Year of vessel's construction")
        vessel_construction_place = models.ForeignKey\
                ('Place',related_name="vessel_construction_place")
        vessel_construction_region = models.ForeignKey\
                ('SpecificRegion', related_name="vessel_construction_region")
        registered_year = models.DateField("Year of vessel's registration")
        registered_place = models.ForeignKey\
                ('Place', related_name="registered_place")
        registered_region = models.ForeignKey\
                ('SpecificRegion', related_name="registered_region")
        owner_of_venture = models.CharField("First owner of venture", max_length=60)
        owners = models.ForeignKey('VoyageVentureOwner')

        # Imputed variables
        imputed_nationality = models.ForeignKey('ImputedCountryShip')
        tonnage_mod = models.DecimalField("Tonnage standardized on British"
                                          "measured tons, 1773-1835",
                                          max_digits=8,
                                          decimal_places=2,
                                          blank=True)


    class VoyageOutcome(models.Model):
        """
        Information about Outcomes
        """

        class ParticularOutcome(models.Model):
            """
            Particular outcome.
            """
            particular_outcome = models.CharField("Outcome label", max_length=70)

        class SlavesOutcome(models.Model):
            """
            Outcome of voyage for slaves.
            """
            slaves_outcome = models.CharField("Outcome label", max_length=70)

        class VesselCapturedOutcome(models.Model):
            """
            Outcome of voyage if vessel captured.
            """
            vessel_captured_outcome = models.CharField("Outcome label",
                                                       max_length=35)

        class OwnerOutcome(models.Model):
            """
            Outcome of voyage for owner.
            """
            owner_outcome = models.CharField("Outcome label", max_length=35)

        class Resistance(models.Model):
            """
            Resistance labels
            """
            resistance_name = models.CharField("Resistance label", max_length=35)

        # Data variables
        particular_outcome = models.ForeignKey('ParticularOutcome')
        resistance = models.ForeignKey('Resistance')

        # Imputed variables
        outcome_slaves = models.ForeignKey('SlavesOutcome')
        vessel_captured_outcome = models.ForeignKey('VesselCapturedOutcome')
        outcome_owner = models.ForeignKey('OwnerOutcome')


    class VoyageItinerary(models.Model):
        """
        Voyage Itinerary data.
        related to: :model:`voyages.apps.voyages.Voyage.BroadRegion`
        related to: :model:`voyages.apps.voyages.Voyage.SpecificRegion`
        related to: :model:`voyages.apps.voyages.Voyage.Place`
        """

        # Data variables
        port_of_departure = models.ForeignKey\
                ('Place', related_name="port_of_departure")
        # Intended variables
        int_first_port_emb = models.ForeignKey\
                ('Place', related_name="int_first_port_emb")
        int_second_port_emb = models.ForeignKey\
                ('Place', related_name="int_second_port_emb")
        int_first_region_purchase_slaves = models.ForeignKey\
                ('SpecificRegion',
                 related_name="int_first_region_purchase_slaves")
        int_second_region_purchase_slaves = models.ForeignKey\
                ('SpecificRegion',
                 related_name="int_second_region_purchase_slaves")
        int_first_port_dis = models.ForeignKey('Place',
                                               related_name=
                                               "int_first_port_dis")
        int_second_port_dis = models.ForeignKey('Place',
                                                related_name=
                                                "int_second_port_dis")
        int_first_region_slave_landing = models.ForeignKey\
                ('SpecificRegion', related_name="int_first_region_slave_landing")
        int_second_region_slave_landing = models.ForeignKey\
                ('SpecificRegion', related_name="int_second_region_slave_landing")

        # End of intended variables
        ports_called_buying_slaves = models.IntegerField("Number of ports "
                                                         "of call prior "
                                                         "to buying slaves",
                                                         max_length=3,
                                                        blank=True)
        first_place_slave_purchase = models.ForeignKey\
                ('Place', related_name="first_place_slave_purchase")
        second_place_slave_purchase = models.ForeignKey\
                ('Place', related_name="second_place_slave_purchase")
        third_place_slave_purchase = models.ForeignKey\
                ('Place', related_name="third_place_slave_purchase")

        first_region_slave_emb = models.ForeignKey('SpecificRegion',
                                                   related_name=
                                                   "first_region_slave_emb")
        second_region_slave_emb = models.ForeignKey('SpecificRegion',
                                                    related_name=
                                                    "second_region_slave_emb")
        third_region_slave_emb = models.ForeignKey('SpecificRegion',
                                                   related_name=
                                                   "third_region_slave_emb")

        port_of_call_before_atl_crossing = models.ForeignKey\
                ('Place', related_name="port_of_call_before_atl_crossing")
        number_of_ports_of_call = models.ForeignKey\
                ('Place', related_name="number_of_ports_of_call")

        first_landing_place = models.ForeignKey\
                ('Place', related_name="first_landing_place")
        second_landing_place = models.ForeignKey\
                ('Place', related_name="second_landing_place")
        third_landing_place = models.ForeignKey\
                ('Place', related_name="third_landing_place")

        first_landing_region = models.ForeignKey\
                ('SpecificRegion', related_name="first_landing_region")
        second_landing_region = models.ForeignKey\
                ('SpecificRegion', related_name="second_landing_region")
        third_landing_region = models.ForeignKey\
                ('SpecificRegion', related_name="third_landing_region")

        place_voyage_ended = models.ForeignKey\
                ('Place', related_name="place_voyage_ended")
        region_of_return = models.ForeignKey\
                ('SpecificRegion', related_name="region_of_return")
        broad_region_of_return = models.ForeignKey\
                ('BroadRegion', related_name="broad_region_of_return")

        # Imputed variables
        imp_port_voyage_begin = models.ForeignKey\
                ('Place', related_name="imp_port_voyage_begin")
        imp_region_voyage_begin = models.ForeignKey\
                ('SpecificRegion', related_name="imp_region_voyage_begin")
        imp_broad_region_voyage_begin = models.ForeignKey\
                ('BroadRegion', related_name="imp_broad_region_voyage_begin")
        principal_place_of_slave_purchase = models.ForeignKey\
                ('Place', related_name="principal_place_of_slave_purchase")
        imp_principal_place_of_slave_purchase = models.ForeignKey\
                ('Place', related_name="imp_principal_place_of_slave_purchase")
        imp_principal_region_of_slave_purchase = models.ForeignKey\
                ('SpecificRegion', related_name=
                "imp_principal_region_of_slave_purchase")
        imp_broad_region_of_slave_purchase = models.\
            ForeignKey('BroadRegion', related_name=
            "imp_broad_region_of_slave_purchase")
        principal_port_of_slave_dis = models.ForeignKey\
                ('Place', related_name="principal_port_of_slave_dis")
        imp_principal_port_slave_dis = models.ForeignKey\
                ('Place', related_name="imp_principal_port_slave_dis")
        imp_principal_region_slave_dis = models.ForeignKey\
                ('SpecificRegion', related_name=""
                "imp_principal_region_slave_dis")
        imp_broad_region_slave_dis = models.ForeignKey\
                ('BroadRegion', related_name="imp_broad_region_slave_dis")


    class VoyageDates(models.Model):
        """
        Voyage dates.
        """

        # Integer variables
        day_voyage_began = models.IntegerField("Day that voyage began",
                                               max_length=2)
        month_voyage_began = models.IntegerField("Month that voyage began",
                                                 max_length=2)
        year_voyage_began = models.IntegerField("Year that voyage began",
                                                max_length=4)

        # Date variables
        voyage_began = models.DateField("Date that voyage began")
        slave_purchase_began = models.DateField("Date that slave "
                                                "purchase began")
        vessel_left_port = models.DateField("Date that vessel left "
                                            "last slaving port")
        first_dis_of_slaves = models.DateField("Date of first disembarkation "
                                               "of slaves")
        arrival_at_second_place_landing = models.DateField(
            "Date of arrival at second place of landing"
        )
        third_dis_of_slaves = models.DateField("Date of third disembarkation"
                                               " of slaves")
        departure_last_place_of_landing = models.DateField("Date of departure "
                                                       "from last place "
                                                       "of landing")
        voyage_completed = models.DateField("Date on which slave voyage "
                                            "completed")


    class VoyageCaptainCrew(models.Model):
        """
        Voyage Captain and Crew.
        """

    class VoyageSlavesNumbers(models.Model):
        """
        Voyage slaves (numbers).
        """

    class VoyageSlavesCharacteristics(models.Model):
        """
        Voyage slaves (characteristics).
        """

    class VoyageSources(models.Model):
        """
        Voyage sources.
        """

    voyage_id = models.AutoField(primary_key=True)
    voyage_in_cdrom = models.IntegerField("Voyage in 1999 CD-ROM", max_length=1,
                                           blank=True)
    voyage_groupings = models.ForeignKey('VoyageGroupings')
    voyage_outcome = models.ForeignKey('VoyageShip')
