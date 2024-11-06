class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_name = request.headers.get("X-Tenant")
        if tenant_name:
            request.tenant = tenant_name
        else:
            request.tenant = "public"  # Default schema

        return self.get_response(request)
