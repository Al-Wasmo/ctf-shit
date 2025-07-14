let modules = 0;
setImmediate(function () {
    const modules = Process.enumerateModules();


    let base = 0;
    modules.forEach(m => {
        if (m.name.toLowerCase().includes("ragnar")) {
            base = m.base;
            console.log(m.name, m.base);
        }
    });


    let target = base.add(0x0068930);
    target = base.add(0x69177);
    let after_strcmp = base.add(0x06917C)
    let after_xor = base.add(0x069621)
    


    Interceptor.attach(ptr(target), function () {
        console.log("JKASDJKAJKDSK")
        const rdi_str = ptr(this.context.rdi).readUtf8String();
        const rsi_str = ptr(this.context.rsi).readUtf8String();

        console.log("    s1 =", rdi_str)
        console.log("    s2 =", rsi_str)
    })




    Interceptor.attach(ptr(after_xor), function () {
        const len = this.context.rdx;
        console.log("len",len)
        const buf = ptr(this.context.rsi).readByteArray(2040);
        console.log("buf",buf)
    })





    Java.perform(function () {
        var Intent = Java.use("android.content.Intent");
        var context = Java.use("android.app.ActivityThread").currentApplication().getApplicationContext();

        var intent = Intent.$new();
        intent.setAction("THE_TRIGER");
        intent.putExtra("key", "6a209693a9acaf10dcd2e425bab62a5e48698b7fc3");
        context.sendBroadcast(intent);

        console.log("[+] Broadcast sent with action THE_TRIGER");
    });

    Java.perform(function () {
        var Intent = Java.use("android.content.Intent");
        var context = Java.use("android.app.ActivityThread").currentApplication().getApplicationContext();

        var intent = Intent.$new();
        intent.setAction("THE_UNLOCKER");
        intent.putExtra("key", "6a209693a9acaf10dcd2e425bab62a5e48698b7fc3");
        context.sendBroadcast(intent);

        console.log("[+] Broadcast sent with action THE_UNLOCKER");
    });

});

