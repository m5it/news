Here's a comprehensive explanation of Nginx domain redirection based on IP using the `map` function, including your additional proxy configuration example:

### Complete Nginx IP-Based Redirection with Map and Proxy

```nginx
http {
    # Create a map that checks the client's IP and returns a backend server
    map $remote_addr $is_local {
        # Local network IPs get marked as 'local'
        192.168.0.0/16    local;
        10.0.0.0/8        local;
        172.16.0.0/12     local;

        # Default case - all other IPs are 'remote'
        default           remote;
    }

    server {
        listen 80;
        server_name example.com;

        location / {
            # Check if the IP is local
            if ($is_local = local) {
                proxy_pass https://192.168.56.242;  # Default for remote
                break;
            }

            # For remote IPs, use the mapped backend
            proxy_pass $is_local;

            # Standard proxy headers
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

### Explanation:

1. **Map Directive**:
   - Creates a lookup table that maps IP addresses to values ('local' or 'remote')
   - Uses CIDR notation for efficient range matching
   - The variable `$is_local` will contain either 'local' or 'remote' based on the client IP

2. **Conditional Proxying**:
   - The `if ($is_local = local)` block checks if the client is in a local network
   - If true, it proxies to `https://192.168.56.242` and breaks out of the block
   - If false, it uses the `$is_local` variable for routing (which would need to be set elsewhere)

3. **Proxy Configuration**:
   - `proxy_pass`: Forwards requests to the backend server
   - `proxy_set_header`: Preserves important client information
   - `X-Real-IP`: Original client IP
   - `X-Forwarded-For`: Chain of proxies
   - `X-Forwarded-Proto`: Original request protocol (http/https)

### Important Notes:

1. The `map` must be defined in the `http` context (outside any `server` blocks)
2. The `if` directive should be used with caution - in this case it's safe as we're using it to set variables
3. For production use, consider:
   - Using SSL/TLS for all connections
   - Adding rate limiting
   - Implementing proper health checks
   - Considering the `geo` module for more complex IP-based routing

Would you like me to modify this configuration for any specific use case or add any additional features?