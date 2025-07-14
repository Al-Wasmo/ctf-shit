Java.perform(function () {
    console.log("=== Frida script loaded ===");
    
    try {
        const TargetClass = Java.use("ctf.l3akctf.pricelessl3ak.h1832fla12");
        console.log("=== Target class found ===");

        // Hook onCreate too to see if the app is being created
        TargetClass.onCreate.implementation = function (bundle) {
            console.log("\n=== [HOOKED] onCreate ===");
            console.log("Bundle: " + bundle);
            
            const intent = this.getIntent();
            if (intent !== null) {
                console.log("Intent Action: " + intent.getAction());
            }
            
            this.onCreate(bundle);
        };

        TargetClass.onNewIntent.implementation = function (intent) {
            console.log("\n=== [HOOKED] onNewIntent ===");
            console.log("Intent Action: " + intent.getAction());
            console.log("Flags: " + intent.getFlags());

            try {
                const extras = intent.getExtras();
                if (extras !== null) {
                    const keys = extras.keySet().toArray();
                    for (let i = 0; i < keys.length; i++) {
                        const key = keys[i];
                        const value = extras.get(key);
                        console.log("Extra[" + key + "] = " + value);
                    }
                } else {
                    console.log("Noo extras in intent.");
                }
            } catch (e) {
                console.log("Error reading extras: " + e);
            }

            // Call original method
            this.onNewIntent(intent);
        };

        console.log("=== Hooks installed successfully ===");
    } catch (e) {
        console.log("Error setting up hooks: " + e);
    }
});

// frida -U -p $(adb shell pidof ctf.l3akctf.pricelessl3akCC) -l inj.js
// adb shell am start -n "ctf.l3akctf.pricelessl3ak/.h1832fla12" -a "BANGO" -f 0x20000000 --es "f" "test_value"
