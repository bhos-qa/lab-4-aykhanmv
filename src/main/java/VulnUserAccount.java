public class VulnUserAccount {

    // Simulated method to fetch user account details by userId
    public String getUserAccountDetails(int userId, int sessionUserId) {
        // Here, userId is passed from the client, and sessionUserId is from the authenticated session

        // IDOR vulnerability: no verification if the userId matches the session user
        // This allows an attacker to supply another user's ID and access their details
        String accountDetails = fetchAccountFromDatabase(userId);

        return accountDetails;
    }

    // Simulated database fetch (vulnerable due to lack of access control)
    private String fetchAccountFromDatabase(int userId) {
        // Normally, this would query the database. We're just simulating data.
        if (userId == 1) {
            return "User 1: John Doe, Balance: $1000";
        } else if (userId == 2) {
            return "User 2: Jane Smith, Balance: $500";
        } else {
            return "User not found";
        }
    }
}
