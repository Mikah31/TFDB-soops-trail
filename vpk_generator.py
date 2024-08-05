import vpk
import struct
import argparse


# Patterns & corresponding base distance
signatures = [[b"\x1f\x05\xe6\x42", 115], [b"\x8f\x02\x7f\x43", 255], # rocket_circle
              [b"\x3d\x0a\xe6\x42", 115], [b"\x1f\x05\x7f\x43", 255], # rocket_circle_color
              [b"\xae\x07\x7f\x43", 255], [b"\x48\x01\x80\x43", 256], # rockettrail
              [b"\x3d\x0a\x7f\x43", 255], [b"\x8f\x02\x80\x43", 256]] # rockettrail_color

# Disabling rocket circle, alpha signatures
additional_signatures = [b"\xf6\x28\x20\x41", # rocket_circle
                         b"\xec\x51\x20\x41"] # rocket_circle_color


def float_to_hex(f):
    return bytearray.fromhex(struct.pack("<f", f).hex())


def generate_VPK(ping, disable_circle):

    try:
        with open("./custom_vpk/particles/rockettrail.pcf", "rb+") as pcf:

            pcf_data = pcf.read()
            modified_pcf = pcf_data

            for sig, base in signatures:
                if sig not in modified_pcf:
                    print(f"Error, could not find {sig}, exiting")
                    exit(0)
                modified_pcf = modified_pcf.replace(sig, float_to_hex(base + ping * 1.75))

            if disable_circle:
                for sig in additional_signatures:
                    if sig not in modified_pcf:
                        print(f"Error, could not find signature to disable circle, continuing")
                        disable_circle = False
                        break
                    modified_pcf = modified_pcf.replace(sig, float_to_hex(0.0))

            pcf.seek(0)
            pcf.write(modified_pcf)

            VPK = vpk.new("./custom_vpk/")
            VPK.save(f"TFDB_{int(ping)}ms{'_no_circle' if disable_circle else ''}.vpk")

            pcf.seek(0)
            pcf.write(pcf_data)

            print("Generated VPK")

    except Exception as e:
        print(e)


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--ping", help="Total amount of latency (ping + interp)")
group = parser.add_mutually_exclusive_group()
group.add_argument("--disable-circle", action="store_true", help="Disables circle")

args = parser.parse_args()

if not args.ping:
    parser.print_help()
    exit(0)

generate_VPK(float(args.ping), args.disable_circle)
