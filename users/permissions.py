from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
	"""Allow users to edit own todos"""

	def has_object_permission(self, request, view, obj):
		"""Check user is trying to edit own todo"""

		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.id == request.user.id