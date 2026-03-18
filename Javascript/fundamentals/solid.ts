class NotificationService {
    send(message: string) {
        throw new Error("Method 'send()' must be implemented.");
    }
}

class MessageFormatter {
    static formatMessage(message: string) {
        return `[ALERT]: ${message}`;
    }
}

class EmailNotification extends NotificationService {
    send( message: string) {
        console.log(`Sending Email: ${message}`);
    }
}

class SMSNotification extends NotificationService {
    send( message: string) {
        console.log(`Sending SMS: ${message}`);
    }
}


class NotificationSender {
    service: any;

    constructor(service: any) {
        this.service = service;
    }

    apply(message: string) {
        const formattedMessage = MessageFormatter.formatMessage(message);
        return this.service.send(formattedMessage)
    }
}


const emailNotification = new EmailNotification()
const smsNotification = new SMSNotification()
const notification = new NotificationSender(smsNotification)

notification.apply("This is a test message for SMS notification.");