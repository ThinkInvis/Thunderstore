import pytest

from thunderstore.community.admin.package_listing import (
    PackageListingAdmin,
    approve_listing,
    reject_listing,
)
from thunderstore.community.models import (
    Community,
    PackageListing,
    PackageListingReviewStatus,
)
from thunderstore.repository.factories import NamespaceFactory
from thunderstore.repository.models import Package, Team


@pytest.mark.django_db
def test_admin_package_listing_approve_listing(
    team: Team, community: Community
) -> None:
    listings = [
        PackageListing.objects.create(
            community=community,
            package=Package.objects.create(
                owner=team,
                name=f"TestPackage{i}",
                namespace=NamespaceFactory.create(team=team),
            ),
            review_status=PackageListingReviewStatus.unreviewed,
        )
        for i in range(5)
    ]

    modeladmin = PackageListingAdmin(PackageListing, None)
    approve_listing(modeladmin, None, PackageListing.objects.all())

    for entry in listings:
        entry.refresh_from_db()
        assert entry.review_status == PackageListingReviewStatus.approved


@pytest.mark.django_db
def test_admin_package_listing_reject_listing(team: Team, community: Community) -> None:
    listings = [
        PackageListing.objects.create(
            community=community,
            package=Package.objects.create(
                owner=team,
                name=f"TestPackage{i}",
                namespace=NamespaceFactory.create(team=team),
            ),
            review_status=PackageListingReviewStatus.unreviewed,
        )
        for i in range(5)
    ]

    modeladmin = PackageListingAdmin(PackageListing, None)
    reject_listing(modeladmin, None, PackageListing.objects.all())

    for entry in listings:
        entry.refresh_from_db()
        assert entry.review_status == PackageListingReviewStatus.rejected


@pytest.mark.django_db
def test_admin_package_listing_readonly_fields(
    active_package_listing: PackageListing,
) -> None:
    modeladmin = PackageListingAdmin(PackageListing, None)
    assert modeladmin.get_readonly_fields(None, None) == []
    assert (
        modeladmin.get_readonly_fields(None, active_package_listing)
        == PackageListingAdmin.readonly_fields
    )
