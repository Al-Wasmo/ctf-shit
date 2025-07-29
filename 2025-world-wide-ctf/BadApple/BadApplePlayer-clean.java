/*
 * Decompiled with CFR 0.152.
 */
import java.io.ByteArrayInputStream;
import java.lang.management.ManagementFactory;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequence;
import javax.sound.midi.Sequencer;

/*
 * Duplicate member names - consider using --renamedupmembers true
 */
public class BadApplePlayer {
    private static long a;
    private static int a;
    private static int b;
    private static byte[] a;
    private static final String[] I;
    private static String[] l;

    public BadApplePlayer() {
        BadApplePlayer llllllllllllllI;
    }

    private static boolean a() {
        for (String str : ManagementFactory.getRuntimeMXBean().getInputArguments()) {
            if (str.contains(I[0]) || str.contains(I[1])) {
                return true;
            }
        }
        return false;
    }

    private static void a(int needed) {
        while (a < needed) {
            if (b >= a.length) {
                b = 0;
                a = 0L;
                a = 0;
            }
            a = a << 8 | (long)(a[b] & 0xFF);
            ++b;
            a += 8;
        }
    }

    private static int a() {
        BadApplePlayer.a(20);
        if ((a >> a - 1 & 1L) == 1L) {
            if ((a >> a - 2 & 1L) == 1L) {
                if ((a >> a - 3 & 1L) == 1L) {
                    if ((a >> a - 4 & 1L) == 1L) {
                        if ((a >> a - 5 & 1L) == 1L) {
                            a -= 5;
                            return 224;
                        }
                        if ((a >> a - 6 & 1L) == 1L) {
                            a -= 6;
                            return 252;
                        }
                        a -= 6;
                        return 63;
                    }
                    if ((a >> a - 5 & 1L) == 1L) {
                        a -= 5;
                        return 7;
                    }
                    a -= 5;
                    return 248;
                }
                if ((a >> a - 4 & 1L) == 1L) {
                    if ((a >> a - 5 & 1L) == 1L) {
                        a -= 5;
                        return 31;
                    }
                    a -= 5;
                    return 128;
                }
                if ((a >> a - 5 & 1L) == 1L) {
                    a -= 5;
                    return 1;
                }
                if ((a >> a - 6 & 1L) == 1L) {
                    if ((a >> a - 7 & 1L) == 1L) {
                        if ((a >> a - 8 & 1L) == 1L) {
                            if ((a >> a - 9 & 1L) == 1L) {
                                a -= 9;
                                return 30;
                            }
                            if ((a >> a - 10 & 1L) == 1L) {
                                a -= 10;
                                return 56;
                            }
                            a -= 10;
                            return 28;
                        }
                        if ((a >> a - 9 & 1L) == 1L) {
                            if ((a >> a - 10 & 1L) == 1L) {
                                if ((a >> a - 11 & 1L) == 1L) {
                                    if ((a >> a - 12 & 1L) == 1L) {
                                        a -= 12;
                                        return 158;
                                    }
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        if ((a >> a - 14 & 1L) == 1L) {
                                            a -= 14;
                                            return 102;
                                        }
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 183;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            if ((a >> a - 17 & 1L) == 1L) {
                                                if ((a >> a - 18 & 1L) == 1L) {
                                                    a -= 18;
                                                    return 77;
                                                }
                                                a -= 18;
                                                return 173;
                                            }
                                            a -= 17;
                                            return 172;
                                        }
                                        a -= 16;
                                        return 233;
                                    }
                                    a -= 13;
                                    return 222;
                                }
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        a -= 13;
                                        return 176;
                                    }
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 80;
                                        }
                                        a -= 15;
                                        return 10;
                                    }
                                    a -= 14;
                                    return 72;
                                }
                                if ((a >> a - 13 & 1L) == 1L) {
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 153;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            if ((a >> a - 17 & 1L) == 1L) {
                                                a -= 17;
                                                return 117;
                                            }
                                            a -= 17;
                                            return 105;
                                        }
                                        a -= 16;
                                        return 167;
                                    }
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        a -= 15;
                                        return 237;
                                    }
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        if ((a >> a - 17 & 1L) == 1L) {
                                            a -= 17;
                                            return 214;
                                        }
                                        if ((a >> a - 18 & 1L) == 1L) {
                                            a -= 18;
                                            return 82;
                                        }
                                        a -= 18;
                                        return 106;
                                    }
                                    if ((a >> a - 17 & 1L) == 1L) {
                                        a -= 17;
                                        return 53;
                                    }
                                    a -= 17;
                                    return 164;
                                }
                                a -= 13;
                                return 140;
                            }
                            a -= 10;
                            return 14;
                        }
                        if ((a >> a - 10 & 1L) == 1L) {
                            a -= 10;
                            return 112;
                        }
                        if ((a >> a - 11 & 1L) == 1L) {
                            if ((a >> a - 12 & 1L) == 1L) {
                                a -= 12;
                                return 121;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 184;
                            }
                            a -= 13;
                            return 9;
                        }
                        if ((a >> a - 12 & 1L) == 1L) {
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 190;
                            }
                            a -= 13;
                            return 216;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            if ((a >> a - 14 & 1L) == 1L) {
                                if ((a >> a - 15 & 1L) == 1L) {
                                    a -= 15;
                                    return 26;
                                }
                                if ((a >> a - 16 & 1L) == 1L) {
                                    if ((a >> a - 17 & 1L) == 1L) {
                                        a -= 17;
                                        return 107;
                                    }
                                    a -= 17;
                                    return 45;
                                }
                                if ((a >> a - 17 & 1L) == 1L) {
                                    a -= 17;
                                    return 218;
                                }
                                a -= 17;
                                return 101;
                            }
                            a -= 14;
                            return 47;
                        }
                        a -= 13;
                        return 57;
                    }
                    if ((a >> a - 8 & 1L) == 1L) {
                        if ((a >> a - 9 & 1L) == 1L) {
                            a -= 9;
                            return 96;
                        }
                        a -= 9;
                        return 6;
                    }
                    if ((a >> a - 9 & 1L) == 1L) {
                        a -= 9;
                        return 225;
                    }
                    a -= 9;
                    return 135;
                }
                if ((a >> a - 7 & 1L) == 1L) {
                    if ((a >> a - 8 & 1L) == 1L) {
                        if ((a >> a - 9 & 1L) == 1L) {
                            a -= 9;
                            return 124;
                        }
                        a -= 9;
                        return 62;
                    }
                    if ((a >> a - 9 & 1L) == 1L) {
                        if ((a >> a - 10 & 1L) == 1L) {
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        a -= 13;
                                        return 27;
                                    }
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 50;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 205;
                                        }
                                        a -= 16;
                                        return 185;
                                    }
                                    a -= 14;
                                    return 244;
                                }
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 49;
                                }
                                a -= 13;
                                return 160;
                            }
                            if ((a >> a - 12 & 1L) == 1L) {
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 156;
                                }
                                if ((a >> a - 14 & 1L) == 1L) {
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 203;
                                        }
                                        a -= 16;
                                        return 229;
                                    }
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        if ((a >> a - 17 & 1L) == 1L) {
                                            if ((a >> a - 18 & 1L) == 1L) {
                                                a -= 18;
                                                return 213;
                                            }
                                            a -= 18;
                                            return 171;
                                        }
                                        if ((a >> a - 18 & 1L) == 1L) {
                                            a -= 18;
                                            return 83;
                                        }
                                        a -= 18;
                                        return 138;
                                    }
                                    a -= 16;
                                    return 139;
                                }
                                a -= 14;
                                return 70;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 29;
                            }
                            a -= 13;
                            return 13;
                        }
                        if ((a >> a - 11 & 1L) == 1L) {
                            if ((a >> a - 12 & 1L) == 1L) {
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 5;
                                }
                                a -= 13;
                                return 238;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                if ((a >> a - 14 & 1L) == 1L) {
                                    a -= 14;
                                    return 108;
                                }
                                if ((a >> a - 15 & 1L) == 1L) {
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        if ((a >> a - 17 & 1L) == 1L) {
                                            a -= 17;
                                            return 89;
                                        }
                                        a -= 17;
                                        return 210;
                                    }
                                    a -= 16;
                                    return 201;
                                }
                                if ((a >> a - 16 & 1L) == 1L) {
                                    if ((a >> a - 17 & 1L) == 1L) {
                                        a -= 17;
                                        return 150;
                                    }
                                    a -= 17;
                                    return 148;
                                }
                                a -= 16;
                                return 197;
                            }
                            if ((a >> a - 14 & 1L) == 1L) {
                                a -= 14;
                                return 38;
                            }
                            if ((a >> a - 15 & 1L) == 1L) {
                                a -= 15;
                                return 217;
                            }
                            if ((a >> a - 16 & 1L) == 1L) {
                                if ((a >> a - 17 & 1L) == 1L) {
                                    a -= 17;
                                    return 91;
                                }
                                a -= 17;
                                return 93;
                            }
                            a -= 16;
                            return 168;
                        }
                        a -= 11;
                        return 243;
                    }
                    a -= 9;
                    return 193;
                }
                a -= 7;
                return 126;
            }
            a -= 2;
            return 0;
        }
        if ((a >> a - 2 & 1L) == 1L) {
            a -= 2;
            return 255;
        }
        if ((a >> a - 3 & 1L) == 1L) {
            if ((a >> a - 4 & 1L) == 1L) {
                if ((a >> a - 5 & 1L) == 1L) {
                    a -= 5;
                    return 254;
                }
                a -= 5;
                return 127;
            }
            if ((a >> a - 5 & 1L) == 1L) {
                if ((a >> a - 6 & 1L) == 1L) {
                    if ((a >> a - 7 & 1L) == 1L) {
                        if ((a >> a - 8 & 1L) == 1L) {
                            if ((a >> a - 9 & 1L) == 1L) {
                                a -= 9;
                                return 131;
                            }
                            if ((a >> a - 10 & 1L) == 1L) {
                                a -= 10;
                                return 227;
                            }
                            a -= 10;
                            return 199;
                        }
                        if ((a >> a - 9 & 1L) == 1L) {
                            if ((a >> a - 10 & 1L) == 1L) {
                                if ((a >> a - 11 & 1L) == 1L) {
                                    if ((a >> a - 12 & 1L) == 1L) {
                                        if ((a >> a - 13 & 1L) == 1L) {
                                            a -= 13;
                                            return 66;
                                        }
                                        a -= 13;
                                        return 119;
                                    }
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        if ((a >> a - 14 & 1L) == 1L) {
                                            a -= 14;
                                            return 18;
                                        }
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 114;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 163;
                                        }
                                        a -= 16;
                                        return 151;
                                    }
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        a -= 14;
                                        return 34;
                                    }
                                    a -= 14;
                                    return 242;
                                }
                                a -= 11;
                                return 207;
                            }
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        a -= 13;
                                        return 67;
                                    }
                                    a -= 13;
                                    return 71;
                                }
                                if ((a >> a - 13 & 1L) == 1L) {
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 215;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 211;
                                        }
                                        if ((a >> a - 17 & 1L) == 1L) {
                                            if ((a >> a - 18 & 1L) == 1L) {
                                                a -= 18;
                                                return 149;
                                            }
                                            if ((a >> a - 19 & 1L) == 1L) {
                                                if ((a >> a - 20 & 1L) == 1L) {
                                                    a -= 20;
                                                    return 85;
                                                }
                                                a -= 20;
                                                return 65535;
                                            }
                                            a -= 19;
                                            return 170;
                                        }
                                        a -= 17;
                                        return 73;
                                    }
                                    a -= 14;
                                    return 76;
                                }
                                a -= 13;
                                return 194;
                            }
                            if ((a >> a - 12 & 1L) == 1L) {
                                if ((a >> a - 13 & 1L) == 1L) {
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        a -= 14;
                                        return 20;
                                    }
                                    a -= 14;
                                    return 100;
                                }
                                a -= 13;
                                return 111;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 226;
                            }
                            if ((a >> a - 14 & 1L) == 1L) {
                                a -= 14;
                                return 98;
                            }
                            if ((a >> a - 15 & 1L) == 1L) {
                                a -= 15;
                                return 155;
                            }
                            if ((a >> a - 16 & 1L) == 1L) {
                                if ((a >> a - 17 & 1L) == 1L) {
                                    a -= 17;
                                    return 75;
                                }
                                a -= 17;
                                return 186;
                            }
                            if ((a >> a - 17 & 1L) == 1L) {
                                a -= 17;
                                return 180;
                            }
                            a -= 17;
                            return 42;
                        }
                        if ((a >> a - 10 & 1L) == 1L) {
                            a -= 10;
                            return 241;
                        }
                        a -= 10;
                        return 143;
                    }
                    a -= 7;
                    return 129;
                }
                if ((a >> a - 7 & 1L) == 1L) {
                    if ((a >> a - 8 & 1L) == 1L) {
                        if ((a >> a - 9 & 1L) == 1L) {
                            a -= 9;
                            return 231;
                        }
                        if ((a >> a - 10 & 1L) == 1L) {
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        if ((a >> a - 14 & 1L) == 1L) {
                                            a -= 14;
                                            return 54;
                                        }
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 187;
                                        }
                                        a -= 15;
                                        return 221;
                                    }
                                    a -= 13;
                                    return 39;
                                }
                                a -= 12;
                                return 132;
                            }
                            if ((a >> a - 12 & 1L) == 1L) {
                                a -= 12;
                                return 33;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 232;
                            }
                            a -= 13;
                            return 228;
                        }
                        if ((a >> a - 11 & 1L) == 1L) {
                            if ((a >> a - 12 & 1L) == 1L) {
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 23;
                                }
                                if ((a >> a - 14 & 1L) == 1L) {
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        a -= 15;
                                        return 175;
                                    }
                                    a -= 15;
                                    return 122;
                                }
                                a -= 14;
                                return 52;
                            }
                            a -= 12;
                            return 152;
                        }
                        if ((a >> a - 12 & 1L) == 1L) {
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 68;
                            }
                            if ((a >> a - 14 & 1L) == 1L) {
                                if ((a >> a - 15 & 1L) == 1L) {
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        a -= 16;
                                        return 182;
                                    }
                                    if ((a >> a - 17 & 1L) == 1L) {
                                        a -= 17;
                                        return 84;
                                    }
                                    a -= 17;
                                    return 81;
                                }
                                a -= 15;
                                return 235;
                            }
                            a -= 14;
                            return 104;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 246;
                        }
                        a -= 13;
                        return 61;
                    }
                    if ((a >> a - 9 & 1L) == 1L) {
                        if ((a >> a - 10 & 1L) == 1L) {
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        a -= 13;
                                        return 204;
                                    }
                                    a -= 13;
                                    return 196;
                                }
                                a -= 12;
                                return 25;
                            }
                            if ((a >> a - 12 & 1L) == 1L) {
                                a -= 12;
                                return 130;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 208;
                            }
                            a -= 13;
                            return 36;
                        }
                        a -= 10;
                        return 247;
                    }
                    if ((a >> a - 10 & 1L) == 1L) {
                        a -= 10;
                        return 239;
                    }
                    a -= 10;
                    return 223;
                }
                if ((a >> a - 8 & 1L) == 1L) {
                    if ((a >> a - 9 & 1L) == 1L) {
                        if ((a >> a - 10 & 1L) == 1L) {
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        if ((a >> a - 14 & 1L) == 1L) {
                                            if ((a >> a - 15 & 1L) == 1L) {
                                                if ((a >> a - 16 & 1L) == 1L) {
                                                    if ((a >> a - 17 & 1L) == 1L) {
                                                        a -= 17;
                                                        return 146;
                                                    }
                                                    a -= 17;
                                                    return 87;
                                                }
                                                a -= 16;
                                                return 147;
                                            }
                                            a -= 15;
                                            return 177;
                                        }
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            if ((a >> a - 16 & 1L) == 1L) {
                                                if ((a >> a - 17 & 1L) == 1L) {
                                                    a -= 17;
                                                    return 181;
                                                }
                                                a -= 17;
                                                return 174;
                                            }
                                            if ((a >> a - 17 & 1L) == 1L) {
                                                a -= 17;
                                                return 154;
                                            }
                                            a -= 17;
                                            return 86;
                                        }
                                        a -= 15;
                                        return 157;
                                    }
                                    a -= 13;
                                    return 236;
                                }
                                a -= 12;
                                return 65;
                            }
                            a -= 11;
                            return 97;
                        }
                        if ((a >> a - 11 & 1L) == 1L) {
                            if ((a >> a - 12 & 1L) == 1L) {
                                a -= 12;
                                return 142;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 200;
                            }
                            a -= 13;
                            return 206;
                        }
                        if ((a >> a - 12 & 1L) == 1L) {
                            a -= 12;
                            return 113;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 95;
                        }
                        if ((a >> a - 14 & 1L) == 1L) {
                            if ((a >> a - 15 & 1L) == 1L) {
                                if ((a >> a - 16 & 1L) == 1L) {
                                    a -= 16;
                                    return 21;
                                }
                                a -= 16;
                                return 37;
                            }
                            a -= 15;
                            return 92;
                        }
                        a -= 14;
                        return 79;
                    }
                    if ((a >> a - 10 & 1L) == 1L) {
                        a -= 10;
                        return 251;
                    }
                    if ((a >> a - 11 & 1L) == 1L) {
                        if ((a >> a - 12 & 1L) == 1L) {
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 220;
                            }
                            a -= 13;
                            return 250;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            if ((a >> a - 14 & 1L) == 1L) {
                                if ((a >> a - 15 & 1L) == 1L) {
                                    a -= 15;
                                    return 161;
                                }
                                a -= 15;
                                return 78;
                            }
                            a -= 14;
                            return 44;
                        }
                        a -= 13;
                        return 188;
                    }
                    if ((a >> a - 12 & 1L) == 1L) {
                        a -= 12;
                        return 99;
                    }
                    if ((a >> a - 13 & 1L) == 1L) {
                        a -= 13;
                        return 59;
                    }
                    a -= 13;
                    return 55;
                }
                if ((a >> a - 9 & 1L) == 1L) {
                    a -= 9;
                    return 4;
                }
                a -= 9;
                return 8;
            }
            a -= 5;
            return 240;
        }
        if ((a >> a - 4 & 1L) == 1L) {
            if ((a >> a - 5 & 1L) == 1L) {
                a -= 5;
                return 192;
            }
            a -= 5;
            return 15;
        }
        if ((a >> a - 5 & 1L) == 1L) {
            a -= 5;
            return 3;
        }
        if ((a >> a - 6 & 1L) == 1L) {
            if ((a >> a - 7 & 1L) == 1L) {
                if ((a >> a - 8 & 1L) == 1L) {
                    if ((a >> a - 9 & 1L) == 1L) {
                        a -= 9;
                        return 16;
                    }
                    a -= 9;
                    return 249;
                }
                if ((a >> a - 9 & 1L) == 1L) {
                    if ((a >> a - 10 & 1L) == 1L) {
                        a -= 10;
                        return 60;
                    }
                    if ((a >> a - 11 & 1L) == 1L) {
                        a -= 11;
                        return 134;
                    }
                    if ((a >> a - 12 & 1L) == 1L) {
                        if ((a >> a - 13 & 1L) == 1L) {
                            if ((a >> a - 14 & 1L) == 1L) {
                                a -= 14;
                                return 88;
                            }
                            a -= 14;
                            return 40;
                        }
                        if ((a >> a - 14 & 1L) == 1L) {
                            if ((a >> a - 15 & 1L) == 1L) {
                                if ((a >> a - 16 & 1L) == 1L) {
                                    if ((a >> a - 17 & 1L) == 1L) {
                                        if ((a >> a - 18 & 1L) == 1L) {
                                            a -= 18;
                                            return 169;
                                        }
                                        a -= 18;
                                        return 165;
                                    }
                                    a -= 17;
                                    return 162;
                                }
                                if ((a >> a - 17 & 1L) == 1L) {
                                    a -= 17;
                                    return 212;
                                }
                                a -= 17;
                                return 90;
                            }
                            a -= 15;
                            return 245;
                        }
                        a -= 14;
                        return 118;
                    }
                    if ((a >> a - 13 & 1L) == 1L) {
                        a -= 13;
                        return 11;
                    }
                    if ((a >> a - 14 & 1L) == 1L) {
                        a -= 14;
                        return 22;
                    }
                    if ((a >> a - 15 & 1L) == 1L) {
                        a -= 15;
                        return 58;
                    }
                    if ((a >> a - 16 & 1L) == 1L) {
                        if ((a >> a - 17 & 1L) == 1L) {
                            a -= 17;
                            return 74;
                        }
                        a -= 17;
                        return 69;
                    }
                    a -= 16;
                    return 41;
                }
                a -= 9;
                return 2;
            }
            if ((a >> a - 8 & 1L) == 1L) {
                if ((a >> a - 9 & 1L) == 1L) {
                    a -= 9;
                    return 32;
                }
                if ((a >> a - 10 & 1L) == 1L) {
                    a -= 10;
                    return 191;
                }
                a -= 10;
                return 253;
            }
            if ((a >> a - 9 & 1L) == 1L) {
                a -= 9;
                return 64;
            }
            a -= 9;
            return 159;
        }
        if ((a >> a - 7 & 1L) == 1L) {
            if ((a >> a - 8 & 1L) == 1L) {
                a -= 8;
                return 24;
            }
            if ((a >> a - 9 & 1L) == 1L) {
                if ((a >> a - 10 & 1L) == 1L) {
                    if ((a >> a - 11 & 1L) == 1L) {
                        if ((a >> a - 12 & 1L) == 1L) {
                            a -= 12;
                            return 198;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 19;
                        }
                        a -= 13;
                        return 35;
                    }
                    if ((a >> a - 12 & 1L) == 1L) {
                        if ((a >> a - 13 & 1L) == 1L) {
                            if ((a >> a - 14 & 1L) == 1L) {
                                if ((a >> a - 15 & 1L) == 1L) {
                                    a -= 15;
                                    return 189;
                                }
                                if ((a >> a - 16 & 1L) == 1L) {
                                    a -= 16;
                                    return 166;
                                }
                                a -= 16;
                                return 43;
                            }
                            if ((a >> a - 15 & 1L) == 1L) {
                                a -= 15;
                                return 179;
                            }
                            a -= 15;
                            return 145;
                        }
                        a -= 13;
                        return 51;
                    }
                    if ((a >> a - 13 & 1L) == 1L) {
                        if ((a >> a - 14 & 1L) == 1L) {
                            a -= 14;
                            return 110;
                        }
                        a -= 14;
                        return 219;
                    }
                    if ((a >> a - 14 & 1L) == 1L) {
                        if ((a >> a - 15 & 1L) == 1L) {
                            if ((a >> a - 16 & 1L) == 1L) {
                                a -= 16;
                                return 209;
                            }
                            if ((a >> a - 17 & 1L) == 1L) {
                                a -= 17;
                                return 234;
                            }
                            a -= 17;
                            return 202;
                        }
                        a -= 15;
                        return 141;
                    }
                    if ((a >> a - 15 & 1L) == 1L) {
                        a -= 15;
                        return 137;
                    }
                    a -= 15;
                    return 94;
                }
                a -= 10;
                return 195;
            }
            a -= 9;
            return 12;
        }
        if ((a >> a - 8 & 1L) == 1L) {
            a -= 8;
            return 120;
        }
        if ((a >> a - 9 & 1L) == 1L) {
            if ((a >> a - 10 & 1L) == 1L) {
                if ((a >> a - 11 & 1L) == 1L) {
                    if ((a >> a - 12 & 1L) == 1L) {
                        a -= 12;
                        return 144;
                    }
                    a -= 12;
                    return 123;
                }
                if ((a >> a - 12 & 1L) == 1L) {
                    a -= 12;
                    return 17;
                }
                a -= 12;
                return 230;
            }
            if ((a >> a - 11 & 1L) == 1L) {
                if ((a >> a - 12 & 1L) == 1L) {
                    a -= 12;
                    return 136;
                }
                a -= 12;
                return 103;
            }
            if ((a >> a - 12 & 1L) == 1L) {
                a -= 12;
                return 125;
            }
            if ((a >> a - 13 & 1L) == 1L) {
                if ((a >> a - 14 & 1L) == 1L) {
                    if ((a >> a - 15 & 1L) == 1L) {
                        a -= 15;
                        return 46;
                    }
                    if ((a >> a - 16 & 1L) == 1L) {
                        a -= 16;
                        return 109;
                    }
                    a -= 16;
                    return 178;
                }
                if ((a >> a - 15 & 1L) == 1L) {
                    a -= 15;
                    return 133;
                }
                a -= 15;
                return 116;
            }
            a -= 13;
            return 115;
        }
        a -= 9;
        return 48;
    }

    private static int huffman_19() {
        BadApplePlayer.a(19);
        if ((a >> a - 1 & 1L) == 1L) {
            if ((a >> a - 2 & 1L) == 1L) {
                a -= 2;
                return 0;
            }
            if ((a >> a - 3 & 1L) == 1L) {
                if ((a >> a - 4 & 1L) == 1L) {
                    if ((a >> a - 5 & 1L) == 1L) {
                        a -= 5;
                        return 128;
                    }
                    a -= 5;
                    return 7;
                }
                if ((a >> a - 5 & 1L) == 1L) {
                    a -= 5;
                    return 31;
                }
                if ((a >> a - 6 & 1L) == 1L) {
                    a -= 6;
                    return 63;
                }
                a -= 6;
                return 240;
            }
            if ((a >> a - 4 & 1L) == 1L) {
                if ((a >> a - 5 & 1L) == 1L) {
                    a -= 5;
                    return 127;
                }
                a -= 5;
                return 224;
            }
            if ((a >> a - 5 & 1L) == 1L) {
                a -= 5;
                return 248;
            }
            if ((a >> a - 6 & 1L) == 1L) {
                a -= 6;
                return 252;
            }
            if ((a >> a - 7 & 1L) == 1L) {
                if ((a >> a - 8 & 1L) == 1L) {
                    if ((a >> a - 9 & 1L) == 1L) {
                        if ((a >> a - 10 & 1L) == 1L) {
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        if ((a >> a - 14 & 1L) == 1L) {
                                            a -= 14;
                                            return 100;
                                        }
                                        a -= 14;
                                        return 34;
                                    }
                                    a -= 13;
                                    return 198;
                                }
                                if ((a >> a - 13 & 1L) == 1L) {
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 219;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 215;
                                        }
                                        a -= 16;
                                        return 167;
                                    }
                                    a -= 14;
                                    return 72;
                                }
                                if ((a >> a - 14 & 1L) == 1L) {
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 163;
                                        }
                                        a -= 16;
                                        return 145;
                                    }
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        if ((a >> a - 17 & 1L) == 1L) {
                                            a -= 17;
                                            return 45;
                                        }
                                        if ((a >> a - 18 & 1L) == 1L) {
                                            if ((a >> a - 19 & 1L) == 1L) {
                                                a -= 19;
                                                return 169;
                                            }
                                            a -= 19;
                                            return 65535;
                                        }
                                        a -= 18;
                                        return 181;
                                    }
                                    a -= 16;
                                    return 91;
                                }
                                if ((a >> a - 15 & 1L) == 1L) {
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        a -= 16;
                                        return 90;
                                    }
                                    a -= 16;
                                    return 221;
                                }
                                a -= 15;
                                return 116;
                            }
                            a -= 11;
                            return 223;
                        }
                        a -= 10;
                        return 28;
                    }
                    if ((a >> a - 10 & 1L) == 1L) {
                        if ((a >> a - 11 & 1L) == 1L) {
                            a -= 11;
                            return 247;
                        }
                        if ((a >> a - 12 & 1L) == 1L) {
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 158;
                            }
                            a -= 13;
                            return 136;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            if ((a >> a - 14 & 1L) == 1L) {
                                a -= 14;
                                return 104;
                            }
                            if ((a >> a - 15 & 1L) == 1L) {
                                if ((a >> a - 16 & 1L) == 1L) {
                                    a -= 16;
                                    return 82;
                                }
                                if ((a >> a - 17 & 1L) == 1L) {
                                    a -= 17;
                                    return 171;
                                }
                                a -= 17;
                                return 180;
                            }
                            if ((a >> a - 16 & 1L) == 1L) {
                                a -= 16;
                                return 175;
                            }
                            a -= 16;
                            return 73;
                        }
                        a -= 13;
                        return 140;
                    }
                    a -= 10;
                    return 56;
                }
                if ((a >> a - 9 & 1L) == 1L) {
                    if ((a >> a - 10 & 1L) == 1L) {
                        a -= 10;
                        return 112;
                    }
                    if ((a >> a - 11 & 1L) == 1L) {
                        a -= 11;
                        return 239;
                    }
                    if ((a >> a - 12 & 1L) == 1L) {
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 57;
                        }
                        a -= 13;
                        return 176;
                    }
                    if ((a >> a - 13 & 1L) == 1L) {
                        if ((a >> a - 14 & 1L) == 1L) {
                            a -= 14;
                            return 79;
                        }
                        if ((a >> a - 15 & 1L) == 1L) {
                            if ((a >> a - 16 & 1L) == 1L) {
                                a -= 16;
                                return 233;
                            }
                            a -= 16;
                            return 147;
                        }
                        a -= 15;
                        return 153;
                    }
                    a -= 13;
                    return 208;
                }
                if ((a >> a - 10 & 1L) == 1L) {
                    a -= 10;
                    return 14;
                }
                if ((a >> a - 11 & 1L) == 1L) {
                    a -= 11;
                    return 191;
                }
                if ((a >> a - 12 & 1L) == 1L) {
                    if ((a >> a - 13 & 1L) == 1L) {
                        a -= 13;
                        return 111;
                    }
                    if ((a >> a - 14 & 1L) == 1L) {
                        a -= 14;
                        return 20;
                    }
                    a -= 14;
                    return 88;
                }
                if ((a >> a - 13 & 1L) == 1L) {
                    if ((a >> a - 14 & 1L) == 1L) {
                        a -= 14;
                        return 188;
                    }
                    if ((a >> a - 15 & 1L) == 1L) {
                        a -= 15;
                        return 122;
                    }
                    if ((a >> a - 16 & 1L) == 1L) {
                        a -= 16;
                        return 201;
                    }
                    if ((a >> a - 17 & 1L) == 1L) {
                        a -= 17;
                        return 165;
                    }
                    a -= 17;
                    return 173;
                }
                if ((a >> a - 14 & 1L) == 1L) {
                    a -= 14;
                    return 61;
                }
                a -= 14;
                return 242;
            }
            if ((a >> a - 8 & 1L) == 1L) {
                if ((a >> a - 9 & 1L) == 1L) {
                    a -= 9;
                    return 2;
                }
                if ((a >> a - 10 & 1L) == 1L) {
                    if ((a >> a - 11 & 1L) == 1L) {
                        if ((a >> a - 12 & 1L) == 1L) {
                            a -= 12;
                            return 97;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 29;
                        }
                        a -= 13;
                        return 80;
                    }
                    if ((a >> a - 12 & 1L) == 1L) {
                        a -= 12;
                        return 152;
                    }
                    if ((a >> a - 13 & 1L) == 1L) {
                        if ((a >> a - 14 & 1L) == 1L) {
                            if ((a >> a - 15 & 1L) == 1L) {
                                if ((a >> a - 16 & 1L) == 1L) {
                                    a -= 16;
                                    return 89;
                                }
                                a -= 16;
                                return 172;
                            }
                            if ((a >> a - 16 & 1L) == 1L) {
                                a -= 16;
                                return 86;
                            }
                            a -= 16;
                            return 77;
                        }
                        a -= 14;
                        return 18;
                    }
                    a -= 13;
                    return 119;
                }
                if ((a >> a - 11 & 1L) == 1L) {
                    if ((a >> a - 12 & 1L) == 1L) {
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 113;
                        }
                        if ((a >> a - 14 & 1L) == 1L) {
                            a -= 14;
                            return 70;
                        }
                        a -= 14;
                        return 68;
                    }
                    a -= 12;
                    return 5;
                }
                if ((a >> a - 12 & 1L) == 1L) {
                    a -= 12;
                    return 103;
                }
                if ((a >> a - 13 & 1L) == 1L) {
                    if ((a >> a - 14 & 1L) == 1L) {
                        if ((a >> a - 15 & 1L) == 1L) {
                            if ((a >> a - 16 & 1L) == 1L) {
                                a -= 16;
                                return 197;
                            }
                            a -= 16;
                            return 81;
                        }
                        if ((a >> a - 16 & 1L) == 1L) {
                            a -= 16;
                            return 168;
                        }
                        a -= 16;
                        return 141;
                    }
                    a -= 14;
                    return 118;
                }
                a -= 13;
                return 23;
            }
            if ((a >> a - 9 & 1L) == 1L) {
                a -= 9;
                return 64;
            }
            if ((a >> a - 10 & 1L) == 1L) {
                if ((a >> a - 11 & 1L) == 1L) {
                    if ((a >> a - 12 & 1L) == 1L) {
                        a -= 12;
                        return 134;
                    }
                    if ((a >> a - 13 & 1L) == 1L) {
                        a -= 13;
                        return 246;
                    }
                    a -= 13;
                    return 156;
                }
                if ((a >> a - 12 & 1L) == 1L) {
                    if ((a >> a - 13 & 1L) == 1L) {
                        a -= 13;
                        return 51;
                    }
                    if ((a >> a - 14 & 1L) == 1L) {
                        a -= 14;
                        return 108;
                    }
                    if ((a >> a - 15 & 1L) == 1L) {
                        if ((a >> a - 16 & 1L) == 1L) {
                            a -= 16;
                            return 117;
                        }
                        a -= 16;
                        return 83;
                    }
                    if ((a >> a - 16 & 1L) == 1L) {
                        a -= 16;
                        return 205;
                    }
                    a -= 16;
                    return 202;
                }
                if ((a >> a - 13 & 1L) == 1L) {
                    a -= 13;
                    return 232;
                }
                a -= 13;
                return 194;
            }
            if ((a >> a - 11 & 1L) == 1L) {
                a -= 11;
                return 195;
            }
            if ((a >> a - 12 & 1L) == 1L) {
                if ((a >> a - 13 & 1L) == 1L) {
                    if ((a >> a - 14 & 1L) == 1L) {
                        if ((a >> a - 15 & 1L) == 1L) {
                            a -= 15;
                            return 58;
                        }
                        if ((a >> a - 16 & 1L) == 1L) {
                            a -= 16;
                            return 107;
                        }
                        a -= 16;
                        return 150;
                    }
                    a -= 14;
                    return 76;
                }
                a -= 13;
                return 184;
            }
            if ((a >> a - 13 & 1L) == 1L) {
                a -= 13;
                return 238;
            }
            a -= 13;
            return 228;
        }
        if ((a >> a - 2 & 1L) == 1L) {
            a -= 2;
            return 255;
        }
        if ((a >> a - 3 & 1L) == 1L) {
            if ((a >> a - 4 & 1L) == 1L) {
                if ((a >> a - 5 & 1L) == 1L) {
                    a -= 5;
                    return 254;
                }
                if ((a >> a - 6 & 1L) == 1L) {
                    if ((a >> a - 7 & 1L) == 1L) {
                        if ((a >> a - 8 & 1L) == 1L) {
                            if ((a >> a - 9 & 1L) == 1L) {
                                a -= 9;
                                return 4;
                            }
                            a -= 9;
                            return 8;
                        }
                        if ((a >> a - 9 & 1L) == 1L) {
                            if ((a >> a - 10 & 1L) == 1L) {
                                if ((a >> a - 11 & 1L) == 1L) {
                                    if ((a >> a - 12 & 1L) == 1L) {
                                        if ((a >> a - 13 & 1L) == 1L) {
                                            if ((a >> a - 14 & 1L) == 1L) {
                                                a -= 14;
                                                return 54;
                                            }
                                            a -= 14;
                                            return 38;
                                        }
                                        a -= 13;
                                        return 250;
                                    }
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        a -= 13;
                                        return 123;
                                    }
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            if ((a >> a - 16 & 1L) == 1L) {
                                                a -= 16;
                                                return 69;
                                            }
                                            a -= 16;
                                            return 211;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 203;
                                        }
                                        a -= 16;
                                        return 179;
                                    }
                                    a -= 14;
                                    return 26;
                                }
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        if ((a >> a - 14 & 1L) == 1L) {
                                            if ((a >> a - 15 & 1L) == 1L) {
                                                if ((a >> a - 16 & 1L) == 1L) {
                                                    a -= 16;
                                                    return 106;
                                                }
                                                a -= 16;
                                                return 105;
                                            }
                                            a -= 15;
                                            return 155;
                                        }
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 94;
                                        }
                                        a -= 15;
                                        return 78;
                                    }
                                    a -= 13;
                                    return 204;
                                }
                                a -= 12;
                                return 65;
                            }
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    if ((a >> a - 13 & 1L) == 1L) {
                                        if ((a >> a - 14 & 1L) == 1L) {
                                            a -= 14;
                                            return 22;
                                        }
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 217;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            if ((a >> a - 17 & 1L) == 1L) {
                                                a -= 17;
                                                return 213;
                                            }
                                            a -= 17;
                                            return 186;
                                        }
                                        a -= 16;
                                        return 148;
                                    }
                                    a -= 13;
                                    return 39;
                                }
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 102;
                                }
                                if ((a >> a - 14 & 1L) == 1L) {
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        a -= 15;
                                        return 133;
                                    }
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        a -= 16;
                                        return 75;
                                    }
                                    a -= 16;
                                    return 209;
                                }
                                a -= 14;
                                return 52;
                            }
                            if ((a >> a - 12 & 1L) == 1L) {
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 36;
                                }
                                a -= 13;
                                return 66;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                if ((a >> a - 14 & 1L) == 1L) {
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        a -= 15;
                                        return 109;
                                    }
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        a -= 16;
                                        return 139;
                                    }
                                    a -= 16;
                                    return 178;
                                }
                                a -= 14;
                                return 50;
                            }
                            a -= 13;
                            return 222;
                        }
                        if ((a >> a - 10 & 1L) == 1L) {
                            a -= 10;
                            return 124;
                        }
                        if ((a >> a - 11 & 1L) == 1L) {
                            if ((a >> a - 12 & 1L) == 1L) {
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 11;
                                }
                                a -= 13;
                                return 55;
                            }
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 200;
                            }
                            a -= 13;
                            return 142;
                        }
                        if ((a >> a - 12 & 1L) == 1L) {
                            a -= 12;
                            return 17;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            if ((a >> a - 14 & 1L) == 1L) {
                                a -= 14;
                                return 44;
                            }
                            if ((a >> a - 15 & 1L) == 1L) {
                                if ((a >> a - 16 & 1L) == 1L) {
                                    a -= 16;
                                    return 166;
                                }
                                a -= 16;
                                return 37;
                            }
                            if ((a >> a - 16 & 1L) == 1L) {
                                a -= 16;
                                return 214;
                            }
                            a -= 16;
                            return 154;
                        }
                        a -= 13;
                        return 67;
                    }
                    if ((a >> a - 8 & 1L) == 1L) {
                        if ((a >> a - 9 & 1L) == 1L) {
                            a -= 9;
                            return 12;
                        }
                        a -= 9;
                        return 120;
                    }
                    if ((a >> a - 9 & 1L) == 1L) {
                        a -= 9;
                        return 32;
                    }
                    a -= 9;
                    return 16;
                }
                if ((a >> a - 7 & 1L) == 1L) {
                    if ((a >> a - 8 & 1L) == 1L) {
                        if ((a >> a - 9 & 1L) == 1L) {
                            if ((a >> a - 10 & 1L) == 1L) {
                                if ((a >> a - 11 & 1L) == 1L) {
                                    if ((a >> a - 12 & 1L) == 1L) {
                                        if ((a >> a - 13 & 1L) == 1L) {
                                            a -= 13;
                                            return 95;
                                        }
                                        a -= 13;
                                        return 19;
                                    }
                                    a -= 12;
                                    return 160;
                                }
                                if ((a >> a - 12 & 1L) == 1L) {
                                    a -= 12;
                                    return 230;
                                }
                                if ((a >> a - 13 & 1L) == 1L) {
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            if ((a >> a - 16 & 1L) == 1L) {
                                                a -= 16;
                                                return 101;
                                            }
                                            a -= 16;
                                            return 74;
                                        }
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 53;
                                        }
                                        a -= 16;
                                        return 146;
                                    }
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        a -= 15;
                                        return 46;
                                    }
                                    a -= 15;
                                    return 183;
                                }
                                if ((a >> a - 14 & 1L) == 1L) {
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        a -= 15;
                                        return 185;
                                    }
                                    a -= 15;
                                    return 92;
                                }
                                if ((a >> a - 15 & 1L) == 1L) {
                                    if ((a >> a - 16 & 1L) == 1L) {
                                        a -= 16;
                                        return 210;
                                    }
                                    a -= 16;
                                    return 43;
                                }
                                a -= 15;
                                return 137;
                            }
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    a -= 12;
                                    return 9;
                                }
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 226;
                                }
                                a -= 13;
                                return 59;
                            }
                            if ((a >> a - 12 & 1L) == 1L) {
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 236;
                                }
                                if ((a >> a - 14 & 1L) == 1L) {
                                    a -= 14;
                                    return 110;
                                }
                                if ((a >> a - 15 & 1L) == 1L) {
                                    a -= 15;
                                    return 229;
                                }
                                if ((a >> a - 16 & 1L) == 1L) {
                                    a -= 16;
                                    return 93;
                                }
                                a -= 16;
                                return 87;
                            }
                            a -= 12;
                            return 216;
                        }
                        a -= 9;
                        return 129;
                    }
                    if ((a >> a - 9 & 1L) == 1L) {
                        if ((a >> a - 10 & 1L) == 1L) {
                            a -= 10;
                            return 193;
                        }
                        a -= 10;
                        return 62;
                    }
                    if ((a >> a - 10 & 1L) == 1L) {
                        if ((a >> a - 11 & 1L) == 1L) {
                            a -= 11;
                            return 243;
                        }
                        a -= 11;
                        return 207;
                    }
                    if ((a >> a - 11 & 1L) == 1L) {
                        if ((a >> a - 12 & 1L) == 1L) {
                            a -= 12;
                            return 130;
                        }
                        a -= 12;
                        return 27;
                    }
                    if ((a >> a - 12 & 1L) == 1L) {
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 196;
                        }
                        a -= 13;
                        return 35;
                    }
                    if ((a >> a - 13 & 1L) == 1L) {
                        a -= 13;
                        return 115;
                    }
                    if ((a >> a - 14 & 1L) == 1L) {
                        if ((a >> a - 15 & 1L) == 1L) {
                            a -= 15;
                            return 237;
                        }
                        a -= 15;
                        return 177;
                    }
                    if ((a >> a - 15 & 1L) == 1L) {
                        if ((a >> a - 16 & 1L) == 1L) {
                            a -= 16;
                            return 234;
                        }
                        if ((a >> a - 17 & 1L) == 1L) {
                            a -= 17;
                            return 149;
                        }
                        a -= 17;
                        return 174;
                    }
                    a -= 15;
                    return 235;
                }
                if ((a >> a - 8 & 1L) == 1L) {
                    if ((a >> a - 9 & 1L) == 1L) {
                        a -= 9;
                        return 30;
                    }
                    a -= 9;
                    return 48;
                }
                if ((a >> a - 9 & 1L) == 1L) {
                    if ((a >> a - 10 & 1L) == 1L) {
                        if ((a >> a - 11 & 1L) == 1L) {
                            if ((a >> a - 12 & 1L) == 1L) {
                                a -= 12;
                                return 144;
                            }
                            a -= 12;
                            return 33;
                        }
                        if ((a >> a - 12 & 1L) == 1L) {
                            if ((a >> a - 13 & 1L) == 1L) {
                                a -= 13;
                                return 40;
                            }
                            a -= 13;
                            return 220;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            if ((a >> a - 14 & 1L) == 1L) {
                                if ((a >> a - 15 & 1L) == 1L) {
                                    a -= 15;
                                    return 218;
                                }
                                if ((a >> a - 16 & 1L) == 1L) {
                                    a -= 16;
                                    return 41;
                                }
                                a -= 16;
                                return 138;
                            }
                            if ((a >> a - 15 & 1L) == 1L) {
                                a -= 15;
                                return 182;
                            }
                            a -= 15;
                            return 187;
                        }
                        a -= 13;
                        return 125;
                    }
                    a -= 10;
                    return 131;
                }
                if ((a >> a - 10 & 1L) == 1L) {
                    if ((a >> a - 11 & 1L) == 1L) {
                        if ((a >> a - 12 & 1L) == 1L) {
                            a -= 12;
                            return 132;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 71;
                        }
                        if ((a >> a - 14 & 1L) == 1L) {
                            if ((a >> a - 15 & 1L) == 1L) {
                                if ((a >> a - 16 & 1L) == 1L) {
                                    a -= 16;
                                    return 162;
                                }
                                a -= 16;
                                return 84;
                            }
                            a -= 15;
                            return 245;
                        }
                        a -= 14;
                        return 114;
                    }
                    if ((a >> a - 12 & 1L) == 1L) {
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 98;
                        }
                        a -= 13;
                        return 206;
                    }
                    a -= 12;
                    return 121;
                }
                a -= 10;
                return 227;
            }
            if ((a >> a - 5 & 1L) == 1L) {
                a -= 5;
                return 3;
            }
            if ((a >> a - 6 & 1L) == 1L) {
                if ((a >> a - 7 & 1L) == 1L) {
                    if ((a >> a - 8 & 1L) == 1L) {
                        if ((a >> a - 9 & 1L) == 1L) {
                            a -= 9;
                            return 126;
                        }
                        a -= 9;
                        return 231;
                    }
                    if ((a >> a - 9 & 1L) == 1L) {
                        if ((a >> a - 10 & 1L) == 1L) {
                            a -= 10;
                            return 199;
                        }
                        a -= 10;
                        return 143;
                    }
                    a -= 9;
                    return 249;
                }
                if ((a >> a - 8 & 1L) == 1L) {
                    a -= 8;
                    return 6;
                }
                a -= 8;
                return 96;
            }
            if ((a >> a - 7 & 1L) == 1L) {
                if ((a >> a - 8 & 1L) == 1L) {
                    if ((a >> a - 9 & 1L) == 1L) {
                        if ((a >> a - 10 & 1L) == 1L) {
                            if ((a >> a - 11 & 1L) == 1L) {
                                if ((a >> a - 12 & 1L) == 1L) {
                                    a -= 12;
                                    return 49;
                                }
                                if ((a >> a - 13 & 1L) == 1L) {
                                    a -= 13;
                                    return 10;
                                }
                                a -= 13;
                                return 244;
                            }
                            if ((a >> a - 12 & 1L) == 1L) {
                                if ((a >> a - 13 & 1L) == 1L) {
                                    if ((a >> a - 14 & 1L) == 1L) {
                                        if ((a >> a - 15 & 1L) == 1L) {
                                            a -= 15;
                                            return 151;
                                        }
                                        a -= 15;
                                        return 189;
                                    }
                                    if ((a >> a - 15 & 1L) == 1L) {
                                        if ((a >> a - 16 & 1L) == 1L) {
                                            a -= 16;
                                            return 212;
                                        }
                                        a -= 16;
                                        return 85;
                                    }
                                    a -= 15;
                                    return 164;
                                }
                                a -= 13;
                                return 190;
                            }
                            a -= 12;
                            return 99;
                        }
                        a -= 10;
                        return 241;
                    }
                    if ((a >> a - 10 & 1L) == 1L) {
                        a -= 10;
                        return 253;
                    }
                    if ((a >> a - 11 & 1L) == 1L) {
                        if ((a >> a - 12 & 1L) == 1L) {
                            a -= 12;
                            return 13;
                        }
                        if ((a >> a - 13 & 1L) == 1L) {
                            a -= 13;
                            return 47;
                        }
                        if ((a >> a - 14 & 1L) == 1L) {
                            if ((a >> a - 15 & 1L) == 1L) {
                                a -= 15;
                                return 161;
                            }
                            a -= 15;
                            return 21;
                        }
                        if ((a >> a - 15 & 1L) == 1L) {
                            if ((a >> a - 16 & 1L) == 1L) {
                                a -= 16;
                                return 42;
                            }
                            a -= 16;
                            return 170;
                        }
                        a -= 15;
                        return 157;
                    }
                    a -= 11;
                    return 25;
                }
                a -= 8;
                return 24;
            }
            if ((a >> a - 8 & 1L) == 1L) {
                if ((a >> a - 9 & 1L) == 1L) {
                    a -= 9;
                    return 159;
                }
                a -= 9;
                return 225;
            }
            if ((a >> a - 9 & 1L) == 1L) {
                if ((a >> a - 10 & 1L) == 1L) {
                    a -= 10;
                    return 60;
                }
                a -= 10;
                return 251;
            }
            a -= 9;
            return 135;
        }
        if ((a >> a - 4 & 1L) == 1L) {
            a -= 4;
            return 1;
        }
        if ((a >> a - 5 & 1L) == 1L) {
            a -= 5;
            return 192;
        }
        a -= 5;
        return 15;
    }

    public static void main(String[] audo_file) {
        int number;
        a = str + new String(I[3]).getBytes(StandardCharsets.ISO_8859_1);


        boolean[][] bool_array = new boolean[240][320];
        Sequencer midi_system = MidiSystem.getSequencer();
        midi_system.open();
        audo_file = MidiSystem.getSequence(new ByteArrayInputStream((byte[])audo_file));
        midi_system.setSequence((Sequence)audo_file);


        System.out.print(I[4]);
        System.out.flush();
        some_str = new String[]{I[5], I[6], I[7]};


        // frame
        for (int i = 0; i < 60; ++i) {
            int j;
            if (i == 0) {
                System.out.print('\u250c');
                for (j = 0; j < 158; ++j) {
                    System.out.print('\u2500');
                }
                System.out.println('\u2510');
                continue;
            }
            if (i == 59) {
                System.out.print('\u2514');
                for (j = 0; j < 158; ++j) {
                    System.out.print('\u2500');
                }
                System.out.print('\u2518');
                continue;
            }
            if (i >= 29 && i < 32) {
                int k;
                j = i - 29;
                String char = some_str[j];
                int number2 = (158 - char.length()) / 2;
                number = (158 - char.length()) % 2;
                System.out.print('\u2502');
                for (k = 0; k < number2; ++k) {
                    System.out.print(I[8]);
                }
                System.out.print(char);
                for (k = 0; k < number2 + number; ++k) {
                    System.out.print(I[9]);
                }
                System.out.println('\u2502');
                continue;
            }
            System.out.print('\u2502');
            for (j = 0; j < 158; ++j) {
                System.out.print(I[10]);
            }
            System.out.println('\u2502');
        }




        System.out.printf(I[11], 33, 81);
        System.out.flush();
        System.in.read();
        System.out.print(I[12]);
        System.out.print(I[13]);



        midi_system.start();
        long i = 0L;
        while (b < a.length) {
            int lllllllllIlllIl;
            int numb;
            int lllllllllIllIIl2;
            int n;
            int lllllllllIllIll2;
            int LEN = BadApplePlayer.huffman_19() & 0xFF | (BadApplePlayer.huffman_19() & 0xFF) << 8;
            byte[] number2 = new byte[150];
            for (number = 0; number < 150; ++number) {
                number2[number] = (byte)BadApplePlayer.huffman_19();
            }
            number = 0;
            boolean[][] k = new boolean[60][160];
            for (int some_str = 0; some_str < 1200 && number < LEN; ++some_str) {
                int lllllllllIllllI;
                lllllllllIllIll2 = some_str / 8;
                n = some_str % 8;
                if ((number2[lllllllllIllIll2] & 1 << n) == 0) continue;
                lllllllllIllIIl2 = some_str % 40;
                numb = some_str / 40;
                for (j = 0; j < 8; ++j) {
                    lllllllllIlllIl = BadApplePlayer.huffman_19();
                    for (int m = 0; m < 8; ++m) {
                        bool_array[(numb << 3) + j][(lllllllllIllIIl2 << 3) + m] = (lllllllllIlllIl >> 7 - m & 1) != 0;
                    }
                }
                for (i = 0; i < 2; ++i) {
                    for (lllllllllIlllIl = 0; lllllllllIlllIl < 4; ++lllllllllIlllIl) {
                        k[(numb << 1) + i][(lllllllllIllIIl2 << 2) + lllllllllIlllIl] = true;
                    }
                }
                ++number;
            }


            Object some_str = new StringBuilder();
            if (LEN > 300) {
                ((StringBuilder)some_str).append(I[14]);
                for (k = 0; k < 60; ++k) {
                    for (n = 0; n < 160; ++n) {
                        ((StringBuilder)some_str).append(BadApplePlayer.a(bool_array, n, k));
                    }
                    if (k >= 59) continue;
                    ((StringBuilder)some_str).append(I[15]);
                }
            } else {
                for (j = 0; j < 60; ++j) {
                    n = 0;
                    while (n < 160) {
                        if (k[j][n]) {
                            lllllllllIllIIl2 = n;
                            while (n < 160 && k[j][n]) {
                                ++n;
                            }
                            numb = n - 1;
                            StringBuilder str_builder = new StringBuilder();
                            for (f = lllllllllIllIIl2; f <= numb; ++f) {
                                str_builder.append(BadApplePlayer.a(bool_array, f, j));
                            }
                            ((StringBuilder)some_str).append(I[16]).append(j + 1).append(';').append(lllllllllIllIIl2 + 1).append('H').append((CharSequence)lllllllllIllllI);
                            continue;
                        }
                        ++n;
                    }
                }
            }

            
            System.out.print(some_str);
            System.out.flush();
            long player_pos = midi_system.getMicrosecondPosition();
            if (player_pos < (i += 33333L)) {
                long lllllllllIllIIl2 = midi_system.isRunning() ? i - player_pos : 33333L;
                Thread.sleep(lllllllllIllIIl2 / 1000L, (int)(lllllllllIllIIl2 % 1000L * 1000L));
                continue;
            }
            i = player_pos + 33333L;
        }
        System.out.print(I[17]);
        midi_system.close();
        BadApplePlayer.a ();
    }


    
    private static char a(boolean[][] pixels, int row, int col) {
        int code = 0;

        // Scale row (y) and col (x) to access 2x4 pixel block
        row <<= 2; // multiply by 4
        col <<= 1; // multiply by 2

        // Bounds check & pixel tests
        if (row < 240 && col < 320 && pixels[row][col])        code |= 0x01;
        if (row + 1 < 240 && pixels[row + 1][col])             code |= 0x02;
        if (row + 2 < 240 && pixels[row + 2][col])             code |= 0x04;
        if (row + 3 < 240 && pixels[row + 3][col])             code |= 0x40;
        if (row < 240 && col + 1 < 320 && pixels[row][col + 1])        code |= 0x08;
        if (row + 1 < 240 && col + 1 < 320 && pixels[row + 1][col + 1]) code |= 0x10;
        if (row + 2 < 240 && col + 1 < 320 && pixels[row + 2][col + 1]) code |= 0x20;
        if (row + 3 < 240 && col + 1 < 320 && pixels[row + 3][col + 1]) code |= 0x80;

        // Lookup character to represent this 2x4 pixel block
        return I[18].charAt(code);
        }

    static {
        BadApplePlayer.init_substr();
        BadApplePlayer.setup_terminal_values();
        a = 0L;
        a = 0;
        b = 0;
    }

    private static void setup_terminal_values() {
        I = new String[19];
        BadApplePlayer.I[0] = BadApplePlayer.blow(l[0], l[1]);
        BadApplePlayer.I[1] = BadApplePlayer.xor_decode(l[2], l[3]);
        BadApplePlayer.I[2] = BadApplePlayer.des_decrypt(l[4], l[5]);

        BadApplePlayer.I[3] = BadApplePlayer.des_decrypt("9Ukf4cvsFzNNl+B3/olHum0HJQ5Zl4bODQ9wvdiXEzwOpml4HcFaefJdWnLUoNiqu5Kq3XRKYnP1SR/hy+wXM02X4Hf+iUe6bQclDlmXhs4ND3C92JcTPA6maXgdwVp58l1actSg2KqHuEk2zm1/ZciXKeoSLM6oRrmwEizA2VUooxlXnAW/Ilahz65l5C60b/nL/qehjBmBx9rs/UmN/TMBRALYRrKHHw6RvKjpHVrQfw9PSudsPiijGVecBb8iVqHPrmXkLrRv+cv+p6GMGYHH2uz9SY39MwFEAthGsocfDpG8qOkdWtB/D09K52w+KKMZV5wFvyJWoc+uZeQutG/5y/6noYwZgcfa7P1Jjf0zAUQC2Eayhx8Okbyo6R1a0H8PT0rnbD4ooxlXnAW/IvutRugqfw/D", "Yyyir");
        BadApplePlayer.I[4] = BadApplePlayer.des_decrypt("CG74vN7titk=", "Xnezh");
        BadApplePlayer.I[5] = BadApplePlayer.blow("5DgmZ40SxnXDwhqEU2Mn7N0FAvLGb4Ct5IovLPFbKAM0tTQsGPFswX0gWJYud6rOWsiQF4//0U9x+bI6M7TDSPnKG+YhD17B", "zIDpX");
        BadApplePlayer.I[6] = BadApplePlayer.xor_decode("FwwzSQoYESMIDxpCNkkFGQwjSRceAyNJEAMSJwYRAhF3KxEXCzsFBlYBPwgRFwEjDBEFTHdXQ+KhpEJr", "vbWic");
        BadApplePlayer.I[7] = BadApplePlayer.xor_decode("JCIwBQZUFTsCEAZwIRlVByQ0BAFafns=", "tPUvu");
        BadApplePlayer.I[8] = BadApplePlayer.xor_decode("RQ==", "ebOAi");
        BadApplePlayer.I[9] = BadApplePlayer.des_decrypt("nwlWvVqWpkg=", "OWngd");
        BadApplePlayer.I[10] = BadApplePlayer.blow("GWqqf9K7DBQ=", "mbueV");
        BadApplePlayer.I[11] = BadApplePlayer.xor_decode("STdVD3Z3CDg=", "RlpkM");
        BadApplePlayer.I[12] = BadApplePlayer.blow("KQdwo72Q1yc=", "NgsYz");
        BadApplePlayer.I[13] = BadApplePlayer.blow("SNCL8E6RunAHedoXguLIKg==", "hyKyw");
        BadApplePlayer.I[14] = BadApplePlayer.blow("eFjKzLVXQrDhlH7LFnJecw==", "mWHlZ");
        BadApplePlayer.I[15] = BadApplePlayer.des_decrypt("UTDQDfEVmw4=", "YQcfb");
        BadApplePlayer.I[16] = BadApplePlayer.des_decrypt("5+wZKWqT600=", "llptX");
        BadApplePlayer.I[17] = BadApplePlayer.xor_decode("cQ1lc28C", "jVZAZ");
        BadApplePlayer.I[18] = BadApplePlayer.des_decrypt("+W3ZSoQaQzb8tsZvhtYf7FsECf16KPOtaLkHkpY2nF+nS2bhVzDH/iQDQzuskkJfZX46oI2ZmSKd+4KOvmdGbjGz69hNUS92R+me+KTVIb5+jaSKSxM2jub6EIu6je+stEsph9QMW0uyDfML4rsK/vyHS3l0ZSgt+8B+6bf+Qtmz6TEXI75mlcEza2r3eM6zF5N7BfSlTx65JwC4ECeBTOS/n5Tt/xLlWFf/e9gQi1e+hFwDEsUqnGTfb8WLSw1ddn95c9XJV5jqe9V7sb7XpO74SkZ4qUpTC03xzPT/R6YYbSKqhw1q1IxlgCuHu9TC32exFUc9ezjHj1h6Db8ARreH/vUE64vim/O1HXcxjZ9W/gJi1PHkVLyK84KlyOr3KaJN6fvrSlstilLg7lvzMLmgd2irpo6xkeGDuIobZdqLaPrUtGqLgZRz3FM7dhUUnFllq0LwGPcyDtGdV+dSPg7LMMRuax5BgqMCwP3/wGEliy0TiQBJNEyfu4DsPe88oFCrwzFUn5GMYaddqL6BHhFHnTM3Yoiadh6rWzRajiI1GO+uTveptyvGgoPjrohrx6hIYN02rRV90odpN1VyxrPrlmGmipQ6Lgh5BQphbxwBytZafe9jnWaXh0GGpJ0+9KfOH6GuFWDBcP+il/QirK8DSlq66XcIhyjtOCAebyiW3hk7UkrIpmdAUZvnQtNwQZG7GGmVGXZZhKlTkEAtAF7QBLylBzdwpyB7N14JnkSY6/PIvu4ljjWcQQOAnVKO74Vb7RgKAV8Vwi25f/NlconyuPpVMJcDwm0TTQ/vB0xKwe4z0qm9JiBGrFbf4SqWj7A1WfKifhNL2N0+fnMjokNft3fBBjYaPc4fv+IEWOCklB2b1NJ9Bex/dKcm+wZ7XKkqRv5KBg9qVNOFgSAWFPG61z9D/sBRHzn3F8gLbPSJ2hROALEZDtyLcZzbiV0oIOgPz6dp0HKKHoELMYhgFU9WtC1dpUije8gjYXYIg7ZMn1ZO9uybgnG64XcQ6YJGxnnZCMt6Sx0=", "Qmfbd");
        l = null;
    }

    private static void init_substr() {
        String file = new Exception().getStackTrace()[0].getFileName();
        l = file.substring(file.indexOf("\u00e4") + 1, file.lastIndexOf("\u00fc")).split("\u00f6");
    }

    private static String xor_decode(String str, String key) {
        str = new String(Base64.getDecoder().decode(str.getBytes(StandardCharsets.UTF_8)), StandardCharsets.UTF_8);
        StringBuilder out = new StringBuilder();
        char[] keyy = key.toCharArray();
        int i = 0;
        for (char char : str.toCharArray()) {
            out.append((char)(char ^ keyy[i % keyy.length]));
            ++i;
        }
        return out.toString();
    }

    private static String des_decrypt(String string, String key) {
        try {
            SecretKeySpec llllllllIllIIIl = new SecretKeySpec(Arrays.copyOf(MessageDigest.getInstance("MD5").digest(key.getBytes(StandardCharsets.UTF_8)), 8), "DES");
            Cipher llllllllIllIIII = Cipher.getInstance("DES");
            llllllllIllIIII.init(2, llllllllIllIIIl);
            return new String(llllllllIllIIII.doFinal(Base64.getDecoder().decode(string.getBytes(StandardCharsets.UTF_8))), StandardCharsets.UTF_8);
        }
        catch (Exception llllllllIlIllll) {
            llllllllIlIllll.printStackTrace();
            return null;
        }
    }

    private static String blow(String llllllllIlIIIIl, String llllllllIlIIIII) {
        try {
            SecretKeySpec llllllllIlIIlII = new SecretKeySpec(MessageDigest.getInstance("MD5").digest(llllllllIlIIIII.getBytes(StandardCharsets.UTF_8)), "Blowfish");
            Cipher llllllllIlIIIll = Cipher.getInstance("Blowfish");
            llllllllIlIIIll.init(2, llllllllIlIIlII);
            return new String(llllllllIlIIIll.doFinal(Base64.getDecoder().decode(llllllllIlIIIIl.getBytes(StandardCharsets.UTF_8))), StandardCharsets.UTF_8);
        }
        catch (Exception llllllllIlIIIlI) {
            llllllllIlIIIlI.printStackTrace();
            return null;
        }
    }
}

