const firebaseConfig = {
    apiKey: "AIzaSyCG4pAXNIr1sjk-PbEwIkRt7a9AWPZdK0U",
    authDomain: "democpp-2577e.firebaseapp.com",
    projectId: "democpp-2577e",
    storageBucket: "democpp-2577e.appspot.com",
    messagingSenderId: "765444663504",
    appId: "1:765444663504:web:77474ac5fc75fb2d0ed6d5"
  };

  // Initialise Firebase
  firebase.initializeApp(firebaseConfig);

  var db = firebase.firestore();

    // ------------ Set Data Function ------------ //
    async function setData(){
        // db.collection("users").doc("testdata").set({
        //     first: "Adam",
        //     last: "Lovelace", 
        //     born: 1815
        // })
        // .then((doc) => {
        //     console.log("Document written with ID testdata");
        // })
        // .catch((error) => {
        //     console.error("Error adding document")
        // });

        await db.collection("users").doc("testdata").set({
            first: "Adam",
            last: "Lovelace", 
            born: 1815
        });
        console.log("Document written with ID testdata")
    }

    // ------------ Read Data Function ------------ //
  async function readData() {
    //   db.collection("users").get()
    //   .then((querySnapshot) => {
    //       querySnapshot.forEach((doc) => {
    //           console.log(doc.data())
    //       })
    //   });
    let res = await db.collection("users").get();
    res.forEach((doc) => {
            console.log(doc.data());
        });
  }

    // ------------ Delete Data Function ------------ //
    async function delData() {
        // db.collection("users").doc("testdata").delete()
        // .then(() => {
        //     console.log("Document successfully deleted!");
        //     window.location.reload()
        // })
        // .catch((error) => {
        //     console.error("Error removing document: ", error);
        // });

        await db.collection("users").doc("testdata").delete();
        console.log("Document successfully deleted!");
    }

    async function btcData() {
        let binance = new ccxt.binance();
        let z = await binance.fetch_ohlcv("BTC/USDT", "5m");
        price = z[499][4];
        console.log(price);
    }
