public class BusinessOperations {

    // 1. Calculate the discount based on the total amount
    public double calculateDiscount(double totalAmount) {
        if (totalAmount > 500) {
            return totalAmount * 0.1; // 10% discount
        }
        return 0;
    }

    // 2. Check product stock availability
    public boolean isProductAvailable(int productId, int quantityRequested) {
        int availableStock = 100;
        return availableStock >= quantityRequested;
    }

    // 3. Calculate total price after applying discount
    public double calculateTotalPrice(double pricePerItem, int quantity, double discount) {
        double total = pricePerItem * quantity;
        return total - discount;
    }

    // 4. Generate an invoice ID based on customer ID and purchase date
    public String generateInvoiceId(int customerId, String purchaseDate) {
        return "INV-" + customerId + "-" + purchaseDate.replaceAll("-", "");
    }

    // 5. Check customer loyalty status based on the total purchases made
    public String checkLoyaltyStatus(double totalPurchases) {
        if (totalPurchases >= 1000) {
            return "Gold";
        } else if (totalPurchases >= 500) {
            return "Silver";
        }
        return "Bronze";
    }

    // 6. Process payment with validation
    public boolean processPayment(String paymentMethod, double amount) {
        if (paymentMethod == null || amount <= 0) {
            return false;
        }
        return true;
    }

    // 7. Send notification to customer
    public void sendNotification(String customerEmail, String message) {
        System.out.println("Notification sent to " + customerEmail + ": " + message);
    }

    // 8. Check if customer is eligible for free shipping
    public boolean isEligibleForFreeShipping(double totalAmount) {
        return totalAmount >= 300;
    }

    // 9. Calculate tax based on location
    public double calculateTax(String location, double amount) {
        double taxRate;
        switch (location) {
            case "NY":
                taxRate = 0.08;
                break;
            case "CA":
                taxRate = 0.075;
                break;
            default:
                taxRate = 0.05;
        }
        return amount * taxRate;
    }

    // 10. Estimate delivery time based on location
    public String estimateDeliveryTime(String location) {
        switch (location) {
            case "NY":
                return "2-3 days";
            case "CA":
                return "4-5 days";
            default:
                return "5-7 days";
        }
    }
}
