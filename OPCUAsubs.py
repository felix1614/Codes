# class SubscriptionHandler:
#     global rawData
#     rawData = []
#
#     def datachange_notification(self, node, val, data):
#         global rawData
#         rawData += (node, val),
#
#     def tagValues(self):
#         global rawData
#         return rawData



# Tags += (await i.read_browse_name()).__dict__["Name"],
            # handler = SubscriptionHandler()
            # subscription = await client.create_subscription(500, handler)
            # await subscription.subscribe_data_change(sensorNodes)
            # await asyncio.sleep(1)
            # Tags = [(await tag.read_browse_name()).__dict__["Name"] for tag in list(zip(*rawValues))[0]]
            # rawVal = list(zip(*rawValues))[1]
            # await subscription.unsubscribe(handler)
            # await subscription.delete()
            # await client.disconnect()
        # return Tags, rawVal