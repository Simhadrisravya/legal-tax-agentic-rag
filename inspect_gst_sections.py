from load_metadata import load_metadata

metadata = load_metadata()

print("Total Metadata Records:", len(metadata))

gst_count = 0

for item in metadata:

    if item.get("document") == "GST_ACT.pdf":

        gst_count += 1

        print(
            "Section:",
            item.get("section")
        )

        if gst_count >= 10:
            break


print("GST Records Found:", gst_count)
