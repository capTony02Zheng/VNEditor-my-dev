from service.module import DBManager
from service.module import GameSlot


db = DBManager.Service("test.db")
db.create_table_if_not_exist("memory")
db.drop_table("memory")
db.close()


memory_service = GameSlot.Service(db_dir="test.db", slot_name="slot1")

memory_service.reset()

memory_service.dump_memory(12)
memory_service.dump_memory(10)
memory_service.dump_memory(17)
memory_service.dump_memory(30)
create_time = memory_service.dump_memory(13)

memory_service.remove_memory(create_time)
memory_service.remove_memory(create_time)

memory_service.print()
