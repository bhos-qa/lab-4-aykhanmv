import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BusinessLogicTest {

    BusinessOperations businessOperations = new BusinessOperations();

    // 1. Test for calculateDiscount method
    @Test
    public void testCalculateDiscount() {
        double totalAmount = 600.0;
        double discount = businessOperations.calculateDiscount(totalAmount);
        assertEquals(60.0, discount, "Discount should be 10% for amounts over 500");

        totalAmount = 300.0;
        discount = businessOperations.calculateDiscount(totalAmount);
        assertEquals(0.0, discount, "Discount should be 0% for amounts less than or equal to 500");
    }

    // 2. Test for isProductAvailable method
    @Test
    public void testIsProductAvailable() {
        int productId = 1;
        int requestedQuantity = 50;
        boolean isAvailable = businessOperations.isProductAvailable(productId, requestedQuantity);
        assertTrue(isAvailable, "Product should be available for quantity less than or equal to 100");

        requestedQuantity = 150;
        isAvailable = businessOperations.isProductAvailable(productId, requestedQuantity);
        assertFalse(isAvailable, "Product should not be available for quantity more than 100");
    }

    // 3. Test for calculateTotalPrice method
    @Test
    public void testCalculateTotalPrice() {
        double pricePerItem = 20.0;
        int quantity = 5;
        double discount = 10.0;
        double totalPrice = businessOperations.calculateTotalPrice(pricePerItem, quantity, discount);
        assertEquals(90.0, totalPrice, "Total price should be calculated correctly with discount applied");

        discount = 0.0;
        totalPrice = businessOperations.calculateTotalPrice(pricePerItem, quantity, discount);
        assertEquals(100.0, totalPrice, "Total price should be calculated correctly without any discount");
    }

    // 4. Test for checkLoyaltyStatus method
    @Test
    public void testCheckLoyaltyStatus() {
        double totalPurchases = 1200.0;
        String loyaltyStatus = businessOperations.checkLoyaltyStatus(totalPurchases);
        assertEquals("Gold", loyaltyStatus, "Loyalty status should be Gold for purchases over 1000");

        totalPurchases = 600.0;
        loyaltyStatus = businessOperations.checkLoyaltyStatus(totalPurchases);
        assertEquals("Silver", loyaltyStatus, "Loyalty status should be Silver for purchases over 500");

        totalPurchases = 400.0;
        loyaltyStatus = businessOperations.checkLoyaltyStatus(totalPurchases);
        assertEquals("Bronze", loyaltyStatus, "Loyalty status should be Bronze for purchases under 500");
    }

    // 5. Test for isEligibleForFreeShipping method
    @Test
    public void testIsEligibleForFreeShipping() {
        double totalAmount = 350.0;
        boolean isEligible = businessOperations.isEligibleForFreeShipping(totalAmount);
        assertTrue(isEligible, "Customer should be eligible for free shipping for amounts over 300");

        totalAmount = 250.0;
        isEligible = businessOperations.isEligibleForFreeShipping(totalAmount);
        assertFalse(isEligible, "Customer should not be eligible for free shipping for amounts under 300");
    }
}
