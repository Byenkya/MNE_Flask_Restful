from me_collector import db


class ProjectDetails(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    groupName = db.Column(db.String(100), nullable=False)
    groupDescription = db.Column(db.String(1000), nullable=False)
    foundingDate = db.Column(db.String(100), nullable=False)
    registered = db.Column(db.Boolean, default=False)
    registrationNumber = db.Column(db.BigInteger, nullable=False)
    registrationDate = db.Column(db.String(100), nullable=False)
    village = db.Column(db.String(100), nullable=False)
    parish = db.Column(db.String(100), nullable=False)
    subCounty = db.Column(db.String(100), nullable=False)
    county = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    subRegion = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    createdBy = db.Column(db.String(100), nullable=False)
    createdOn = db.Column(db.String(100), nullable=False)
    uuid = db.Column(db.String(100), nullable=False)
    memberShipNumber = db.Column(db.BigInteger, nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    otherName = db.Column(db.String(100), nullable=False, default="")
    gender = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(100), nullable=False)
    paid = db.Column(db.Boolean, default=False)
    memberRole = db.Column(db.String(100), nullable=False)
    memberPhotoPath = db.Column(db.String(200), nullable=False)
    otherDetails = db.Column(db.String(1000), nullable=False)
    projectNumber = db.Column(db.BigInteger, nullable=False)
    projectName = db.Column(db.String(100), nullable=False)
    projectFocus = db.Column(db.String(5000), nullable=False)
    startDate = db.Column(db.String(100), nullable=False)
    endDate = db.Column(db.String(100), nullable=False)
    expectedDate = db.Column(db.String(100), nullable=False)
    fundedBy = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.BigInteger, nullable=False)
    teamLeader = db.Column(db.String(100), nullable=False)
    teamLeaderEmail = db.Column(db.String(100), nullable=False)
    teamLeaderPhone = db.Column(db.String(100), nullable=False)
    otherProjectContacts = db.Column(db.String(500), nullable=False)
    projectDescription = db.Column(db.String(10000), nullable=False)
    assessmentDate = db.Column(db.String(100), nullable=False)
    assessMilestone = db.Column(db.Boolean, default=False)
    assessedBy = db.Column(db.String(100), nullable=False)
    assessmentFor = db.Column(db.String(100), nullable=False)
    observation = db.Column(db.String(10000), nullable=False)
    photoOnePath = db.Column(db.String(200), nullable=False)
    photoTwoPath = db.Column(db.String(200), nullable=False)
    photoThreePath = db.Column(db.String(200), nullable=False)
    photoFourPath = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    altitude = db.Column(db.String, nullable=True)
    gpsCrs = db.Column(db.String(100), nullable=True)
    milestoneDate = db.Column(db.String(100), nullable=False)
    milestoneDetails = db.Column(db.String(10000), nullable=False)
    milestoneTarget = db.Column(db.String(10000), nullable=False)
    milestoneTargetDate = db.Column(db.String(100), nullable=False)
    assignedTo = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    mileStoneComments = db.Column(db.String(10000), nullable=False)
    milestonePhotoOnePath = db.Column(db.String(200), nullable=False)
    milestonePhotoTwoPath = db.Column(db.String(200), nullable=False)
    milestonePhotoThreePath = db.Column(db.String(200), nullable=False)
    milestonePhotoFourPath = db.Column(db.String(200), nullable=False)


class PdmAssets(db.Model):
    __tablename__ = 'pdm_assets'
    id = db.Column(db.BigInteger, primary_key=True)
    geom = db.Column(db.String)
    uuid = db.Column(db.String(254), nullable=False)
    group_name = db.Column(db.String(254), nullable=False)
    group_id = db.Column(db.Float, nullable=False)
    lat_x = db.Column(db.Float, nullable=False)
    lon_y = db.Column(db.Float, nullable=False)
    asset_id = db.Column(db.String(254), nullable=False)
    date_acquired = db.Column(db.Date, nullable=False)
    asset_name = db.Column(db.String(254), nullable=False)
    person_incharge = db.Column(db.String(254), nullable=False)
    asset_description = db.Column(db.String(2000), nullable=False)
    asset_photo1 = db.Column(db.String(254), nullable=False)
    asset_photo2 = db.Column(db.String(254), nullable=False)
    created_by = db.Column(db.String(254), nullable=False)
    date_created = db.Column(db.Date, nullable=False)
    updated_by = db.Column(db.String(254), nullable=False)
    date_updated = db.Column(db.Date, nullable=False)

class PdmBeneficiaries(db.Model):
    __tablename__ = 'pdm_beneficiaries'
    id = db.Column(db.BigInteger, primary_key=True)
    geom = db.Column(db.String)
    uuid = db.Column(db.String(254), nullable=False)
    other_name = db.Column(db.String(254), nullable=False)
    last_name = db.Column(db.String(254), nullable=False)
    member_id = db.Column(db.Float, nullable=False)
    nin = db.Column(db.String(254), nullable=False)
    gender = db.Column(db.String(254), nullable=False)
    contact = db.Column(db.Float, nullable=False)
    email = db.Column(db.Float, nullable=False)
    status = db.Column(db.Float, nullable=False)
    subsistenc = db.Column(db.BigInteger, nullable=False)
    district = db.Column(db.String(254), nullable=False)
    subcounty = db.Column(db.String(254), nullable=False)
    parish = db.Column(db.String(254), nullable=False)
    village = db.Column(db.String(254), nullable=False)
    created_by = db.Column(db.String(254), nullable=False)
    date_creat = db.Column(db.String(254), nullable=False)
    updated_by = db.Column(db.String(254), nullable=False)
    date_updat = db.Column(db.String(254), nullable=False)
    group_name = db.Column(db.String(254), nullable=False)
    group_id = db.Column(db.Float, nullable=False)
    lat_x = db.Column(db.Float, nullable=False)
    lon_y = db.Column(db.Float, nullable=False)





