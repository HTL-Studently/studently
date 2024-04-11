<script>
    import { onMount } from 'svelte';
    import QRCode from 'qrcode';
  
    export let paymentData;

    let qrCodeDataUrl = '';
    
  
    async function generatePaymentQRCode() {
    try {
      const formattedData = formatPaymentData(paymentData);
      const dataUrl = await QRCode.toDataURL(formattedData);
      qrCodeDataUrl = dataUrl;
    } catch (err) {
      console.error(err);
    }
}

function formatPaymentData(data) {
    // This is a simplified example. You'll need to format the data according to the EPC QR Code specification.
    // For example, you might need to concatenate fields with specific separators, encode the data in a specific format, etc.
    return `BCD\n001\n1\nSCT\n${data.BIC}\n${data.merchantName}\n${data.iban}\nEUR${data.transactionAmount}\n\n${data.purpose}`;
  }
  
    // Generate the QR code when the component mounts
    onMount(generatePaymentQRCode);
  </script>
  
  <img src={qrCodeDataUrl} alt="Payment QR Code" />