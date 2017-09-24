// "AmbiLightClient.cpp": Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"
#include <windows.h>
#include <stdarg.h>

#define LOG_DEBUG log

void log(const char* format, ...)
{
	const int MAX_SIZE = 1024;
	char buf[MAX_SIZE];
	wchar_t wbuf[MAX_SIZE];
	va_list argptr;
	va_start(argptr, format);
	vsprintf_s(buf, format, argptr);
	va_end(argptr);

	size_t sz = strlen(buf);
	if (sz + 1 < MAX_SIZE)
	{
		buf[sz] = '\n';
		buf[sz + 1] = '\0';
	}

	size_t outSize;
	mbstowcs_s(&outSize, wbuf, buf, MAX_SIZE -1);
	OutputDebugStringW(wbuf);
}


int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, char*, int nShowCmd)
{
	HDC dc = GetDC(NULL);
	POINT cursor;
	GetCursorPos(&cursor);
	COLORREF color = GetPixel(dc, cursor.x, cursor.y);
	int red = GetRValue(color);
	int green = GetGValue(color);
	int blue = GetBValue(color);

	LOG_DEBUG("red: %d", red);
	LOG_DEBUG("green: %d", green);
	LOG_DEBUG("blue: %d", blue);

	ReleaseDC(NULL, dc);
    return 0;
}

