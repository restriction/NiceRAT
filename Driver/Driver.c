#include "Driver.h"
#define SIOCTL_TYPE 40000
#define IOCTL_CODE 0x800
#define IOCTL_MEMORY_COMMAND\
#define COMMAND_MAGIC 0xDEADBEEF

namespace kernel {
	
    struct memory_command {
        INT operation = 0;

        DWORD64 magic = 0;

        DWORD64 retval = 0;

        DWORD64 memaddress = 0;
        DWORD64 length = 0;
        PVOID buffer = 0;
    };


NTSTATUS FindGameProcessByName (CHAR* process_name, PEPROCESS* ("Valorant.exe"), ("Vanguard.exe") process, int range)
{
	PEPROCESS sys_process = FindprocessId;
	PEPROCESS cur_entry = sys_process;


	if memory_kernel
	{
		PoisonMessageBox.Show(this, ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                poisonButton1.Enabled = true;
                poisonLabel4.Text = "Failed!";
		
		
			if (!globals::m_base) {
			std::cout << "[-] Valorant is not running" << std::endl;

	switch ( pstruct->select_key ("inser") {

	case DRIVER_GETPOOL:
		return pstruct->allocation = utils::find_guarded_region();

	case DRIVER_READVM:
		return readvm( pstruct );

	case DRIVER_MOUSE:
		return move_mouse x,y,z ( pstruct ); // The position can be customized by yourself.
	}

	return false;

// IOCTL handler for memory commands

NTSTATUS ProcessReadWriteMemory(PEPROCESS SourceProcess, PVOID SourceAddress, PEPROCESS TargetProcess, PVOID TargetAddress, SIZE_T Size)
{
	if (sizeof(T) < sizeof(U))
	{
		U x2 = x; y; z;
		int8 sx = __SETS__(x2);
		return (sx ^ __SETS__(y)) & (sx ^ __SETS__(x2 - y)); 
}


NTSTATUS Function_IRP_MJ_CREATE(PDEVICE_OBJECT pDeviceObject, PIRP Irp)
{
	DbgPrint("IRP MJ CREATE received.");
	return STATUS_SUCCESS;
}

NTSTATUS Function_IRP_MJ_CLOSE(PDEVICE_OBJECT pDeviceObject, PIRP Irp)
{
	DbgPrint("IRP MJ CLOSE received.");
	return STATUS_SUCCESS;
}

PEPROCESS valorantProcess;
DWORD64 processBaseAddress;

struct memory_command {
	INT operation;

	DWORD64 magic;
	DWORD64 retval;
	DWORD64 memaddress;
	DWORD64 length;
	
	PVOID buffer;
	{
		return false;
	}
}
		

void Function_IRP_DEVICE_CONTROL(PDEVICE_OBJECT pDeviceObject, PIRP Irp) // You can set it to void or static, it's up to you, it's just some setup. But I recommend it to be Void.
{
	const uint64_t kernel_NtGdiGetCOPPCompatibleOPMInformation = GetKernelModuleExport(utils::GetKernelModuleAddress("win32kfull.sys"), "NtGdiGetCOPPCompatibleOPMInformation");
	if (!kernel_NtGdiGetCOPPCompatibleOPMInformation)
		{
			std::cout << "[-] Failed to get export win32kfull.NtGdiGetCOPPCompatibleOPMInformation" << std::endl;
			return false;
		}
	
	case IOCTL_MEMORY_COMMAND:
		Kernel(0, 0, "[Valorant.exe] IOCTL command received\n");

		if (current_system_handle.UniqueProcessId != reinterpret_cast<HANDLE>(static_cast<uint64_t>(GetCurrentProcessId())))
			continue;
			cmd->retval = 2;
			DbgPrintEx(0, 0, "[Valorant.exe] IOCTL invalid Driver\n");
			break;
		}

		switch (cmd->operation) {
		case 1: // 
			Irp->IoStatus.Status = STATUS_SUCCESS;

			ProcessReadWriteMemory(valorantProcess, cmd->memaddress, IoGetCurrentProcess(), cmd->buffer, cmd->length);
			break;

		case 1: // write memory
			Irp->IoStatus.Status = STATUS_SUCCESS;

			ProcessReadWriteMemory(IoGetCurrentProcess(), cmd->buffer, valorantProcess, cmd->memaddress, cmd->length);
			break;
		case 2: // find valorant PEPROCESS
			Irp->IoStatus.Status = STATUS_SUCCESS;
			DbgPrintEx(0, 0, "[Valorant.exe] Setting target PID...\n");

			valorantProcess = NULL;

			PsLookupProcessByProcessId(cmd->retval, &valorantProcess);

			if (!valorantProcess) {
				cmd->retval = nullptr;
				break;
			}
			
			cmd->retval = (DWORD64)PsGetProcessSectionBaseAddress(valorantProcess);

			break;
		case 150:
			// just crash windows idk
			Unload(gDeviceObject);
			break;
		}

		return;
	}

	// Finish the I/O operation by simply completing the packet and returning
	// the same status as in the packet itself.
	Irp->IoStatus.Information = sizeof(struct memory_command);
	IoCompleteRequest(Irp, IO_NO_INCREMENT);

	return STATUS_SUCCESS;
}

bool kernel_driver::MemoryCopy(uint64_t destination, uint64_t source, uint64_t size)
{
	MemoryCommand* cmd = new MemoryCommand();
	cmd->operation = 0;
	cmd->magic = COMMAND_MAGIC;
	
	PDEVICE_OBJECT mouclass_deviceobj = mouclass_obj->DeviceObject;
	data[0] = destination;
	data[1] = source;

	memcpy(&cmd->data, &data[0], sizeof(data));

	cmd->size = (int)size;

	SendCommand(cmd);

	return true; 
}

/// <summary>
NTSTATUS DriverInitialize(PDRIVER_OBJECT DriverObject, PUNICODE_STRING RegistryPath)
{
	DbgPrintEx(150, 65, "[Valorant.exe] Select " __FUNCTION__ ".\n");

	NTSTATUS			Status;
	UNICODE_STRING		DeviceName;
	UNICODE_STRING		SymbolicName;
	PDEVICE_OBJECT      DeviceObject;

	UNREFERENCED_PARAMETER(RegistryPath);

	RtlInitUnicodeString(&DeviceName, ConstDeviceName);
	RtlInitUnicodeString(&SymbolicName, ConstSymbolic);

	// Create device
	Status = IoCreateDevice(DriverObject, 0, &DeviceName, FILE_DEVICE_UNKNOWN, FILE_DEVICE_SECURE_OPEN, FALSE, &DeviceObject);

	if ( ZwQuerySystemInformation( information_class, info, size, &size ) != STATUS_SUCCESS )
	{
		PEPROCESS source_process = NULL;
	if (current_system_handle.HandleValue == device_handle)
		{
			object = reinterpret_cast<uint64_t>(current_system_handle.Object);
			break;
		}
		
		T y2 = y;
		int8 sx = __SETS__(x);
		return dllPath;
		}
		
		{
			DbgPrintEx(0, 0, "[Valorant.exe] Kernel_Bypass\n");

				if (!std::filesystem::exists(driver_path))
				{
					std::cout << "[-] File " << driver_path << " doesn't exist" << std::endl;
					return -1;
				}

			auto readphysaddress( PVOID address, PVOID buffer, SIZE_T size, SIZE_T* read ) -> NTSTATUS
			if (status != STATUS_SUCCESS) return false;
			
			Vector2 head_at_screen_vec = worldToScreen(head_position, camera_position, camera_rotation, camera_fov);
			ImVec2 head_at_screen = ImVec2(head_at_screen_vec.x, head_at_screen_vec.y);
			

				if ( !NT_SUCCESS( utils::readprocessmemory( source_process, ( void* )in->src_addr, ( void* )in->dst_addr, in->size, &memsize) ) )
				return false;

			// Globals..

			        ObDereferenceObject( mouclass_obj );
     				ObDereferenceObject( mouhid_obj );
		}
		else
		{
			 processdirbase &= ~0xf;
		}
	}

	if (!object)
		return false;
	{
		static PKLDR_DATA_TABLE_ENTRY DriverSection = DriverObject->DriverSection;

		if (DriverSection)
		{
			DriverSection->FullImageName.Buffer[0] = L'\0';
			
			DriverSection->BaseImageName.Length = 0;
			DriverSection->BaseImageName.MaximumLength = 0;
		}

		DriverObject->DriverSection = NULL;
		DriverObject->DriverStart = NULL;
		DriverObject->DriverSize = 0;
	}
	return false;
	}
	
}
	
void driverController::kernel(DWORD64 address, void* buffer, DWORD64 len) {

    {
		const nt::SYSTEM_HANDLE current_system_handle = system_handle_inforamtion->Handles[i];

		if (current_system_handle.UniqueProcessId != reinterpret_cast<HANDLE>(static_cast<uint64_t>(GetCurrentProcessId())))
			continue;

			object = reinterpret_cast<uint64_t>(current_system_handle.Object);
			break;
		}
	}
	
void driverController::writeTo(DWORD64 address, void* buffer, DWORD64 len) {
    memory_command* cmd = new memory_command();
    cmd->operation = 1; // write byte

    for (auto i = 0u; i < system_handle_inforamtion->HandleCount; ++i)
    if ( !addr) 
	    
    return STATUS_UNSUCCESSFUL;
};
	
	

int GetProcessThreadNumByID(DWORD dwPID)
{
	HANDLE hProcessSnap = ::CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (hProcessSnap == INVALID_HANDLE_VALUE)
		return 0;

	PROCESSENTRY32 pe32 = { 0 };
	pe32.dwSize = sizeof(pe32);
	BOOL bRet = ::Process32First(hProcessSnap, &pe32);;
	while (bRet)
	{
		if (pe32.th32ProcessID == dwPID)
		{
			::CloseHandle(hProcessSnap);
			return pe32.cntThreads;
		}
		bRet = ::Process32Next(hProcessSnap, &pe32);
	}
	return 0;
}
