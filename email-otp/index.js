const nodemailer = require('nodemailer');
const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors())

const transporter = nodemailer.createTransport({
    service: process.env.SERVICE,
    port : 465,
    auth: {
        user: `${USERNAME}`,
        pass: `${PASSWORD}`
    }
});

let otpPairs = {}; // {email: otp}

app.get('/', (req, res) => {
    res.send('Hello World!');
});

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

app.get('/sendmail', (req, res) => {
    res.header("Access-Control-Allow-Origin", "*")
    const otp = Math.floor(getRandomArbitrary(100000,999999))

    const mailOptions = {
        from: `${USERNAME}`,
        to: req.query.to,
        subject: `${APP_NAME} Email Verification`,
        text: `Dear User,

Thank you for creating an account on our ${APP_NAME}. To ensure the security of your account, we require you to complete the OTP verification process.

Please enter the following OTP to verify your account: ${otp}.

Note: This OTP is valid for only 10 minutes. Please do not share this OTP with anyone, including our customer support team.

If you did not create an account on our application, please ignore this email.

Thank you for choosing ${APP_NAME} We look forward to providing you with the best service.

Best regards,
${APP_NAME} Team`
    };

    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            console.log(error);
            res.send('Error');
        } else {
            console.log('Email sent: ' + info.response);
            res.send('Email sent');
            otpPairs[req.query.to] = otp;
        }
    });

    setInterval(()=>{
        delete otpPairs[req.query.to];
    },600000)
});


app.get('/verifyotp', (req, res) => {
    res.header("Access-Control-Allow-Origin", "*")
    const otp = req.query.otp
    const email = req.query.email
    if(otpPairs[email]!=undefined && otp == otpPairs[email]) {
        delete otpPairs[email];
        res.send('OTP Verified');
    }
    else {
        res.send('OTP Not Verified');
    }
});

app.listen(process.env.PORT || 3000, () => {
    console.log('Server is running on port 3000');
});