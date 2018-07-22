import os
import sys
import unittest as t

path = os.path.abspath(os.path.dirname(__file__)) + '/..'
sys.path.append(path)

from stack import *
# from kspvar import KspVarObj
from interfaces import IOutput
# from interfaces import IName
from native_types import kInt
from native_types import kArrInt
from native_types import kStr
from native_types import kReal
from native_types import KspNativeArray

from dev_tools import DevTest
# from dev_tools import unpack_lines
from dev_tools import expand_if_callable

from abstract import KSP
# from abstract import KspObject

from loops import For


class TestStackArray(DevTest, t.TestCase):

    def test_types(self):
        ref_types = {
            'int': kArrInt,
            'str': kArrStr,
            'real': kArrReal
        }
        int_arr = [0] * 3
        int_arr[0] = StackArray('intArr0', kArrInt, 100)
        int_arr[1] = StackArray('intArr1', kInt, 100)
        int_arr[2] = StackArray('intArr2', int, 100)

        for idx, item in enumerate(int_arr):
            self.assertIsInstance(item, StackArray)
            self.assertEqual(len(item), 100)
            self.assertIsInstance(item.seq, ref_types['int'])
            item[1] = 2
            self.assertEqual(item[1], 2)

        str_arr = [0] * 3
        str_arr[0] = StackArray('strArr0', kArrStr, 100)
        str_arr[1] = StackArray('strArr1', kStr, 100)
        str_arr[2] = StackArray('strArr2', str, 100)

        for idx, item in enumerate(str_arr):
            self.assertIsInstance(item, StackArray)
            self.assertEqual(len(item), 100)
            self.assertIsInstance(item.seq, ref_types['str'])
            item[1] = 2
            self.assertEqual(item[1], 2)

        real_arr = [0] * 3
        real_arr[0] = StackArray('realArr0', kArrReal, 100)
        real_arr[1] = StackArray('realArr1', kReal, 100)
        real_arr[2] = StackArray('realArr2', float, 100)

        for idx, item in enumerate(real_arr):
            self.assertIsInstance(item, StackArray)
            self.assertEqual(len(item), 100)
            self.assertIsInstance(item.seq, ref_types['real'])
            item[1] = 2
            self.assertEqual(item[1], 2)

    def test_methods_test(self):
        KSP.toggle_test_state(True)
        self.methods()

    def test_methods_compile(self):
        KSP.toggle_test_state(False)
        self.methods()

    def methods(self):
        arr = StackArray('intArr', kArrInt, 100)
        with For(arr=arr) as gen:
            for idx, val in enumerate(gen):
                arr[idx] = idx
        if KSP.is_under_test():
            arr_vals = arr()
            for i in range(100):
                self.assertEqual(arr_vals[i], i)
                self.assertEqual(arr[i], i)
        else:
            with self.assertRaises(KspNativeArray.error):
                for i in arr:
                    pass
            arr[99] = 99
            self.assertEqual(IOutput.get()[-1],
                             '%intArr[99] := 99')
            self.assertEqual(arr(), '%intArr')

        with self.assertRaises(KspNativeArray.error):
            arr.append(2)
        with self.assertRaises(KspNativeArray.error):
            arr.extend([2])


class TestFrameVar(DevTest, t.TestCase):

    def setUp(self):
        super().setUp()
        self.arr = StackArray('intStackArr', int, 100)
        self.Int = kInt('int', 2)
        self.y = kInt('y', 3)
        self.IntArr = kArrInt('intArr', [1, 2, 3], length=3)
        self.StrArr = StackArray('strStackArr', str, 100)

    def test_main_test(self):
        KSP.toggle_test_state(True)
        self.main()

    def test_main_code(self):
        KSP.toggle_test_state(False)
        self.main()

    def main(self):
        x = FrameVar('x', self.Int)
        arr = FrameVar('arr', self.IntArr)
        val = FrameVar('val', 1)
        loc_int = FrameVar('loc_int', self.arr,
                           length=1, start_idx=0)
        # tmp = kLocArrInt('loc_arr_temp', length=4)
        loc_arr = FrameVar('loc_arr', self.arr,
                           length=4, start_idx=1)
        loc_str = FrameVar('string', self.StrArr,
                           length=1, start_idx=5)

        self.assertEqual(x.len, 1)
        self.assertEqual(arr.len, 3)
        self.assertEqual(val.len, 1)
        self.assertEqual(loc_int.len, 1)
        self.assertEqual(loc_arr.len, 4)
        self.assertEqual(loc_str.len, 1)

        self.assertEqual(x(), self.Int())
        # print(x(), self.Int())
        self.assertEqual(arr(), self.IntArr())
        self.assertEqual(val(), 1)
        self.assertEqual(loc_int(), 0)
        with self.assertRaises(AssertionError):
            self.assertEqual(loc_arr(), 1)
        self.assertEqual(loc_arr[0], 0)
        self.assertEqual(loc_str(), '')

        with self.assertRaises(IndexError):
            loc_arr[4] = 1

        arr[2] = 4
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                f'{self.IntArr.name()}[2] := 4')
        else:
            self.assertEqual(arr[2], 4)

        loc_int(1)
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                f'{self.arr.name()}[0] := 1')
        else:
            self.assertEqual(self.arr[0], 1)

        loc_str(1)
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                f'{self.StrArr.name()}[5] := 1')
        else:
            self.assertEqual(self.StrArr[5], '1')

        loc_str += '1'
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                f'{self.StrArr.name()}[5] := ' +
                f'{self.StrArr.name()}[5] & "1"')
        else:
            self.assertEqual(loc_str(), '11')

        loc_arr[0] = 2
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                f'{self.arr.name()}[1] := 2')
        else:
            self.assertEqual(self.arr[1], 2)

        loc_arr[3] = 3
        with For(arr=loc_arr) as gen:
            for idx, val in enumerate(gen):
                self.assertEqual(val, loc_arr[idx])
                pass

        if KSP.is_under_test():
            self.assertEqual(loc_arr[self.y], 3)
        else:
            self.assertEqual(
                loc_arr[self.y](),
                '%intStackArr[1 + $y]')


@t.skip
class TestStackFrame(DevTest, t.TestCase):

    def setUp(self):
        super().setUp()
        self.intvar = \
            FrameVar('intvar', kInt('intvar', 2))
        self.strvar = \
            FrameVar('strvar', kStr('strvar', 'str'))
        self.arr = \
            FrameVar('arrInt', kArrInt('arrInt', [1, 2, 3, 4]))

    def tearDown(self):
        super().tearDown()

    def test_main_code(self):
        KSP.toggle_test_state(False)
        self.main()

    def test_main_return(self):
        KSP.toggle_test_state(True)
        self.main()

    def main(self):
        frame = StackFrame()

        frame.append('int', self.intvar)
        self.assertEqual(frame.size, 1)
        if KSP.is_under_test():
            self.assertEqual(frame['int'](), 2)
        else:
            self.assertEqual(frame['int'](), '$intvar')

        frame.append('str', self.strvar)
        self.assertEqual(frame.size, 2)
        if KSP.is_under_test():
            self.assertEqual(frame['str'](), 'str')
        else:
            self.assertEqual(frame['str'](), '@strvar')

        frame.append('arr', self.arr)
        self.assertEqual(frame.size, 6)
        if KSP.is_under_test():
            self.assertEqual(frame['arr'](), [1, 2, 3, 4])
        else:
            self.assertEqual(frame['arr'](), '%arrInt')

        with self.assertRaises(AssertionError) as e:
            frame.append('arr', self.arr)
        self.assertEqual(f'{e.exception}', 'var exists')

        with self.assertRaises(AssertionError) as e:
            frame.append('new', 1)
        self.assertEqual(f'{e.exception}',
                         f'has to be {FrameVar}')

        with self.assertRaises(AssertionError) as e:
            frame.append(2, self.arr)
        self.assertEqual(f'{e.exception}', 'key has to be str')

        f_int, f_str, f_arr = [var for var in frame]
        self.assertIs(f_int, frame['int'])
        self.assertIs(f_str, frame['str'])
        self.assertIs(f_arr, frame['arr'])

        frame_vars = [var for var in frame]
        for idx, item in enumerate(frame.items()):
            self.assertIs(item, frame_vars[idx])

    def test_extend(self):
        frame = StackFrame()
        frame.extend(int=self.intvar,
                     str=self.strvar, arr=self.arr)

        frame_vars = self.intvar, self.strvar, self.arr
        for idx, item in enumerate(frame.items()):
            self.assertIs(item, frame_vars[idx])


push_lines = [
    'inc($_for_loop_curr_idx)',
    '%_for_loop_idx[$_for_loop_curr_idx] := 0',
    'while(%_for_loop_idx[$_for_loop_curr_idx] < 100000)',
    '%stack_int_arr[%stack_int_idx[$stack_int_curr]' +
    ' + 0 + %_for_loop_idx[$_for_loop_curr_idx]]' +
    ' := %full_arr[%_for_loop_idx[$_for_loop_curr_idx]]',
    'inc(%_for_loop_idx[$_for_loop_curr_idx])', 'end while',
    'dec($_for_loop_curr_idx)',
    '%stack_int_arr[%stack_int_idx[$stack_int_curr] + 100000] := $x'
]


@t.skip
class TestStack(DevTest, t.TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_types(self):
        stack = Stack('intstack', 1000, kInt)
        self.assertIsInstance(stack.idx_curr, kInt)
        self.assertIsInstance(stack.arr, StackArray)
        self.assertIsInstance(stack.arr.seq, kArrInt)
        self.assertIsInstance(stack.idx_arr, kArrInt)

        stack = Stack('strstack', 1000, kStr)
        self.assertIsInstance(stack.idx_curr, kInt)
        self.assertIsInstance(stack.arr, StackArray)
        self.assertIsInstance(stack.arr.seq, kArrStr)
        self.assertIsInstance(stack.idx_arr, kArrInt)

    def test_push_returns(self):
        KSP.toggle_test_state(True)
        self.push()

    def test_push_code(self):
        KSP.toggle_test_state(False)
        self.push()

    def push(self):
        stack = Stack('int', 1000000, kInt)
        full = kArrInt('full_arr', [i for i in range(100000)])
        x = kInt('x', 4)
        stack.push(full=full, x=x)
        if not KSP.is_under_test():
            self.assertEqual(IOutput.get(), push_lines)

        frame = stack.peek()
        full, x = frame.items()
        if KSP.is_under_test():
            self.assertEqual(full[1], 1)
            self.assertEqual(full[2], 2)
        else:
            self.assertEqual(
                full[1],
                '%stack_int_arr' +
                '[%stack_int_idx[$stack_int_curr] + 0 + 1]')
        if KSP.is_under_test():
            self.assertEqual(x(), 4)
        else:
            self.assertEqual(
                full[1],
                '%stack_int_arr' +
                '[%stack_int_idx[$stack_int_curr] + 0 + 100000]')
        x += 1
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                '%stack_int_arr[%stack_int_idx[$stack_int_curr]' +
                ' + 100000] := %stack_int_arr[%stack_int_idx' +
                '[$stack_int_curr] + 100000] + 1')
            self.assertEqual(
                x(),
                '%stack_int_arr[%stack_int_idx' +
                '[$stack_int_curr] + 100000]')
        else:
            self.assertEqual(x(), 4)

        full[1] += 1
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                '%stack_int_arr[%stack_int_idx[$stack_int_curr]' +
                ' + 0 + 1] := %stack_int_arr[%stack_int_idx' +
                '[$stack_int_curr] + 0 + 1] + 1')
            self.assertEqual(
                full[1](),
                '%stack_int_arr[%stack_int_idx' +
                '[$stack_int_curr] + 0 + 1]')
        else:
            self.assertEqual(full[1], 2)

        stack.pop()
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                '$stack_int_curr := $stack_int_curr - 1')

    def test_local_return(self):
        KSP.toggle_test_state(True)
        self.local()

    # @t.skip
    def test_local_code(self):
        KSP.toggle_test_state(False)
        self.local()

    def local(self):
        stack = Stack('int', 1000000, kInt)
        x = kLocal(int)
        arrY = kLocal(int, 10)
        stack.push(x=x, arrY=arrY)

        frame = stack.peek()
        x, arrY = frame.items()
        if not KSP.is_under_test():
            self.assertEqual(
                expand_if_callable(x()),
                "%stack_int_arr[%stack_int_idx[$stack_int_curr] + 0]")
            self.assertEqual(
                expand_if_callable(arrY[9]),
                '%stack_int_arr[%stack_int_idx[$stack_int_curr]' +
                ' + 1 + 9]')
        with self.assertRaises(IndexError):
            arrY[10]

        arrY[2] = 5
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                '%stack_int_arr[%stack_int_idx[$stack_int_curr]' +
                ' + 1 + 2] := 5')
        else:
            self.assertEqual(arrY[2], 5)
        x += 1
        if not KSP.is_under_test():
            self.assertEqual(
                IOutput.get()[-1],
                '%stack_int_arr[%stack_int_idx[$stack_int_curr] + 0]' +
                ' := %stack_int_arr[%stack_int_idx' +
                '[$stack_int_curr] + 0] + 1')
        else:
            self.assertEqual(x(), 1)


if __name__ == '__main__':
    t.main()
