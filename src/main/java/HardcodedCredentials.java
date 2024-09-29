public class HardcodedCredentials {

    // Vulnerable method with hardcoded credentials
    public boolean authenticate(String username, String password) {
        // Hardcoded admin credentials (vulnerable)
        String adminUsername = "admin";
        String adminPassword = "P@ssw0rd123";  // Vulnerability: Hardcoded password

        // Check if provided credentials match the hardcoded ones
        if (username.equals(adminUsername) && password.equals(adminPassword)) {
            return true;  // Authentication successful
        }
        return false;  // Authentication failed
    }
}
