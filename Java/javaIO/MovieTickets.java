package javaIO;
import javax.swing.JOptionPane;

public class MovieTickets {

    public static void main(String[] args){


        String movie_name ;
        String inputStr ;
        String outputStr ;

        double adult_ticket_price ;
        double child_ticket_price ;
        double percentage_to_donate ;

        double gross_amount ;
        double net_sale ;
        double amount_donated ;

        int adult_tickets_count ;
        int child_tickets_count ;


        movie_name = JOptionPane.showInputDialog("Enter movie name: ");

        inputStr = JOptionPane.showInputDialog("Enter adult ticket price: ");
        adult_ticket_price = Double.parseDouble(inputStr);

        inputStr = JOptionPane.showInputDialog("Enter child ticket price: ");
        child_ticket_price = Double.parseDouble(inputStr);

        inputStr = JOptionPane.showInputDialog("Number of adult tickets sold: ");
        adult_tickets_count = Integer.parseInt(inputStr);

        inputStr = JOptionPane.showInputDialog("Number of child tickets sold: ");
        child_tickets_count = Integer.parseInt(inputStr);

        inputStr = JOptionPane.showInputDialog("Percentage donated to charity: ");
        percentage_to_donate = Double.parseDouble(inputStr);

        gross_amount = (adult_ticket_price * adult_tickets_count) + (child_ticket_price * child_tickets_count);

        amount_donated = percentage_to_donate * gross_amount;

        net_sale = gross_amount - amount_donated;

        outputStr = "Movie name: " + movie_name + "\n"
                + "Number of Tickets Sold: " + (adult_tickets_count + child_tickets_count) + "\n"
                + "Gross amount: $" + String.format("%.2f", gross_amount) + "\n"
                + "Percentage of the Gross Amount Donated: " + String.format("%.2f%%", percentage_to_donate) + "\n"
                + "Amount Donated: $" + String.format("%.2f", amount_donated) + "\n"
                + "Net Sale: $" + String.format("%.2f", net_sale);

        JOptionPane.showMessageDialog(null, outputStr, "Theatre Sales Data", JOptionPane.INFORMATION_MESSAGE);

        System.exit(0);

    }
}
