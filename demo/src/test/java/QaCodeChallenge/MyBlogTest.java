package QaCodeChallenge;
import java.time.Duration;
import java.util.Iterator;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
//import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.edge.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


public class MyBlogTest {

         public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.edge.driver","C:\\Users\\Rahul\\Selenium\\demo\\src\\main\\resources\\Drivers\\msedgedriver.exe");

        WebDriver driver = new EdgeDriver();
        String Url = "https://blog-five-pink-87.vercel.app/";
        driver.get(Url);
        driver.manage().window().maximize();


        //Page title test
        if(driver.getTitle().contains("MyBlg"))
        System.out.println("Page title contains: " + driver.getTitle());
        else
        System.out.println("Page title contains: " + driver.getTitle());

        //Page url test
        if(driver.getCurrentUrl().contains(Url))
        System.out.println("Page url contains: " + driver.getCurrentUrl());
        else
        System.out.println("Page url contains: " + driver.getCurrentUrl());

        
        //Toggle Button test       
       
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15));
        WebElement toggleButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@aria-label='Toggle dark mode']")));
        toggleButton.click();
        Thread.sleep(3000); 
        
        String dataState = toggleButton.getAttribute("data-state");
        
        if ("on".equals(dataState)) {
            System.out.println("The toggle button is in the ON state.");
        } else if ("off".equals(dataState)) {
            System.out.println("The toggle button is in the OFF state.");
        } else {
            System.out.println("Unexpected state: " + dataState);
        }
      
        
               

       //Urls test home page

      List<WebElement> allURLs = driver.findElements(By.tagName("a"));
      System.out.println("Total links on the Wb Page: " + allURLs.size());

      Iterator<WebElement> iterator = allURLs.iterator();
      while (iterator.hasNext()) {
    	  Url = iterator.next().getText();
    	  System.out.println(Url);
      }

             

        // comments Testing
        
        driver.findElement(By.cssSelector(".text-2xl.font-semibold.mb-2")).click();      
        
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//textarea[@placeholder='Add comment...']"))).sendKeys("This is a comments section testing...");
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//button[text()='Comment']"))).click();
        driver.close();


      





}

}